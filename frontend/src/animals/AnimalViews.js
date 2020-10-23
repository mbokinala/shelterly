import React, {useEffect, useState} from 'react';
import axios from "axios";
import { Link } from 'raviger';
import Moment from 'react-moment';
import { Carousel } from 'react-responsive-carousel';
import { Card, Col, ListGroup, OverlayTrigger, Tooltip } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faBandAid, faClipboardList, faCut, faEdit, faShieldAlt, faWarehouse
} from '@fortawesome/free-solid-svg-icons';
import "react-responsive-carousel/lib/styles/carousel.min.css";

const header_style = {
  textAlign: "center",
}

export function AnimalView({id}) {

  const [images, setImages] = useState([]);

  // Initial animal data.
  const [data, setData] = useState({
    owner: null,
    request: null,
    name: '',
    species: '',
    sex: '',
    size: '',
    age: '',
    pcolor: '',
    scolor: '',
    color_notes: '',
    fixed: 'unknown',
    aggressive: 'unknown',
    confined: 'unknown',
    injured: 'unknown',
    behavior_notes: '',
    last_seen: null,
    front_image: null,
    side_image: null,
    extra_images: [],
    action_history: [],
    full_address:'',
    owner_object: {first_name:'', last_name:'', phone:'', email:''}
  });

  // Hook for initializing data.
  useEffect(() => {
    let source = axios.CancelToken.source();
    const fetchAnimalData = async () => {
      // Fetch Animal data.
      await axios.get('/animals/api/animal/' + id + '/', {
        cancelToken: source.token,
      })
      .then(response => {
        setData(response.data);
        var image_urls = [];
        image_urls = image_urls.concat(response.data.front_image||[]).concat(response.data.side_image||[]).concat(response.data.extra_images);
        setImages(image_urls);
      })
      .catch(error => {
        console.log(error.response);
      });
    };
    fetchAnimalData();
  }, [id]);

  return (
    <>
    <div className="row mt-3" style={{marginBottom:"-8px"}}>
      <div className="col-12 d-flex">
        <h1 style={header_style}>
          Animal Details - {data.status}<Link href={"/animals/animal/edit/" + id}> <FontAwesomeIcon icon={faEdit} inverse /></Link>
        </h1>
      </div>
    </div>
    <hr/>
    <div className="row mb-2">
      <div className="col-6 d-flex" style={{marginRight:"-15px"}}>
        <Card className="border rounded d-flex" style={{width:"100%"}}>
          <Card.Body>
            <Card.Title>
              <h4>Information
              {data.confined === 'yes' ?
                <OverlayTrigger
                  key={"confined"}
                  placement="top"
                  overlay={
                    <Tooltip id={`tooltip-confined`}>
                      Animal is confined
                    </Tooltip>
                  }
                >
                  <FontAwesomeIcon icon={faWarehouse} size="sm" className="ml-1" />
                </OverlayTrigger> :
              ""}
              {data.fixed === 'yes' ?
                <OverlayTrigger
                  key={"fixed"}
                  placement="top"
                  overlay={
                    <Tooltip id={`tooltip-fixed`}>
                      Animal is fixed or neutered
                    </Tooltip>
                  }
                >
                  <FontAwesomeIcon icon={faCut} size="sm" className="ml-1" />
                </OverlayTrigger> :
              ""}
              {data.aggressive === 'yes' ?
                <OverlayTrigger
                  key={"aggressive"}
                  placement="top"
                  overlay={
                    <Tooltip id={`tooltip-aggressive`}>
                      Animal is aggressive
                    </Tooltip>
                  }
                >
                  <FontAwesomeIcon icon={faShieldAlt} size="sm" className="ml-1" />
                </OverlayTrigger> :
              ""}
              {data.injured === 'yes' ?
                <OverlayTrigger
                  key={"injured"}
                  placement="top"
                  overlay={
                    <Tooltip id={`tooltip-injured`}>
                      Animal is injured
                    </Tooltip>
                  }
                >
                  <FontAwesomeIcon icon={faBandAid} size="sm" className="ml-1" />
                </OverlayTrigger> :
              ""}
            </h4>
            </Card.Title>
            <hr/>
            <ListGroup variant="flush" style={{marginTop:"-13px", marginBottom:"-13px", textTransform:"capitalize"}}>
              <ListGroup.Item>
                <div className="row">
                  <span className="col"><b>Name:</b> {data.name||"Unknown"}</span>
                </div>
              </ListGroup.Item>
              <ListGroup.Item>
                <div className="row">
                  <span className="col-6"><b>Species:</b> {data.species}</span>
                  <span className="col-6"><b>Sex:</b> {data.sex||"Unknown"}</span>
                </div>
              </ListGroup.Item>
              <ListGroup.Item>
                <div className="row">
                  <span className="col-6"><b>Age:</b> {data.age||"Unknown"}</span>
                  <span className="col-6"><b>Size:</b> {data.size}</span>
                </div>
              </ListGroup.Item>
              {data.last_seen ? <ListGroup.Item><b>Last Seen:</b> <Moment format="LLL">{data.last_seen}</Moment></ListGroup.Item> : ""}
            </ListGroup>
            <hr/>
            <Card.Title>
              <h4 className="mb-0">Owner<span style={{fontSize:18}}>{data.owner_object.first_name !== 'Unknown' ? <Link href={"/hotline/owner/" + data.owner}> <FontAwesomeIcon icon={faClipboardList} size="sm" inverse /></Link>:""}<Link href={"/hotline/owner/edit/" + data.owner}> <FontAwesomeIcon icon={faEdit} size="sm" inverse /></Link></span></h4>
            </Card.Title>
            <ListGroup variant="flush" style={{marginTop:"-13px", marginBottom:"-13px"}}>
              <ListGroup.Item><b>Name: </b>{data.owner_object.first_name} {data.owner_object.last_name}</ListGroup.Item>
              {data.owner_object.phone ? <ListGroup.Item><b>Telephone: </b>{data.owner_object.phone}</ListGroup.Item> : ""}
              {data.owner_object.email ? <ListGroup.Item><b>Email: </b>{data.owner_object.email}</ListGroup.Item> : ""}
            </ListGroup>
            <hr/>
            <Card.Title>
              <h4 className="mb-0">Location</h4>
            </Card.Title>
            <ListGroup variant="flush">
              <ListGroup.Item style={{marginTop:"-13px"}}><b>Address:</b> {data.full_address}</ListGroup.Item>
            </ListGroup>
          </Card.Body>
        </Card>
      </div>
      <Col xs={6} className="pr-0" style={{width:"100%"}}>
        <div className="slide-container flex-grow-1 border rounded pl-0 pr-0" style={{width:"auto", height:"322px"}}>
          <Carousel className="carousel-wrapper" showThumbs={false} showStatus={false}>
            {images.map(image => (
              <div key={image} className="image-container">
                <img src={image} />
              </div>
            ))}
          </Carousel>
        </div>
        <Card className="border rounded d-flex mt-3" style={{width:"100%"}}>
          <Card.Body>
            <Card.Title>
              <h4>Description</h4>
            </Card.Title>
            <hr/>
            <ListGroup variant="flush">
              <ListGroup.Item style={{marginTop:"-13px", textTransform:"capitalize"}}>
              <div className="row">
                <span className="col-6"><b>Primary Color:</b> {data.pcolor||"N/A"}</span>
                <span className="col-6"><b>Secondary Color:</b> {data.scolor||"N/A"}</span>
              </div>
              </ListGroup.Item>
              {data.color_notes ? <ListGroup.Item><b>Color Notes:</b> {data.color_notes}</ListGroup.Item> : ""}
              {data.behavior_notes ? <ListGroup.Item><b>Behavior Notes:</b> {data.behavior_notes}</ListGroup.Item> : ""}
            </ListGroup>
          </Card.Body>
        </Card>
      </Col>
    </div>
    {data.action_history.map(action => (
      <p key={action}>{action}</p>
    ))}
    </>
  );
};
