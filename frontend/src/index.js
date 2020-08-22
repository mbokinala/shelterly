import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'bootswatch/dist/darkly/bootstrap.min.css';
import { CookiesProvider } from 'react-cookie';
import * as serviceWorker from './serviceWorker';
import Shelterly from './Shelterly';
import { AuthProvider } from './accounts/AccountsReducer';

ReactDOM.render(<CookiesProvider><AuthProvider><Shelterly /></AuthProvider></CookiesProvider>, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
