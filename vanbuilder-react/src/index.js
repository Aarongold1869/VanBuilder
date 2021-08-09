import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './custom.scss';
import App from './App';
import reportWebVitals from './reportWebVitals';
import * as serviceWorker from './serviceWorker';

import { BuildListComponent } from './builder'
import { LandingPage } from './main_pages';
import { navbar } from './navbar'

const appEl = document.getElementById('root')
if (appEl) {
    ReactDOM.render(<App />, appEl);
}

const e = React.createElement

// navbar element
const navBarEl = document.querySelectorAll(".navbar")
navBarEl.forEach(container=> {
    ReactDOM.render(
        e(navbar, container.dataset), container);
})

// landing page component
const landingEl = document.querySelectorAll(".landing-page")
landingEl.forEach(container=> {
    ReactDOM.render(
        e(LandingPage, container.dataset), container);
})

const BuildListEl = document.querySelectorAll('.build-list')
BuildListEl.forEach(container=> {
    ReactDOM.render(
        e(BuildListComponent, container.dataset), container);
})

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
serviceWorker.unregister();
