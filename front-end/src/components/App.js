import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import {connect} from 'react-redux';

import './styles.css';

import Auth from './Auth';
import Credit from './Credit';
import Dashboard from './Dashboard';
import Devices from './Devices';
import Header from './Header';
import Home from './Home';
import Logon from './Logon';
import PrivateRoute from './PrivateRoute';
import Quiz from './Quiz';
import Social from './Social';
import Score from './Score';

class App extends Component {
  render() {
    return (
        <BrowserRouter>
          <div className="App">
            <Header />
            <Switch>
              <Route path="/auth" component={Auth} />
              <Route path="/credit" component={Credit} />
              <Route path="/devices" component={Devices} />
              <PrivateRoute
                component={Dashboard}
                user={this.props.user}
                path="/dashboard"
              />
              <Route path="/logon" component={Logon} />
              <Route path="/quiz" component={Quiz} />
              <Route path="/social" component={Social} />
              <Route path="/score" component={Score} />
              <Route path="/" component={Home} />
            </Switch>
          </div>
        </BrowserRouter>
    );
  }
}

let mapStateToProps = function(state) {
  return {
    user: state.user
  }
}

export default connect(mapStateToProps, null)(App);
