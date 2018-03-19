import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import promiseMiddlware from 'redux-promise';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import App from './components/App';
import reducers from './reducers';

const createStoreWithMiddleware = applyMiddleware(promiseMiddlware)(createStore);

ReactDOM.render(
  <Provider store={createStoreWithMiddleware(reducers)}>
    <App />
  </Provider>
  , document.querySelector('.container'));
