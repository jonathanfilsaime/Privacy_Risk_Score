import React from 'react';
import { Route, Redirect } from 'react-router-dom'

const PrivateRoute = (props) => {
  let Component = props.component;
  let returnedComponent;

  if (/*props.user.loggedIn*/ true) {
    returnedComponent = ( <Component {...props}/> );
  } else {
    returnedComponent = (
      <Redirect to={{
        pathname: '/logon',
        state: { from: props.location }
      }}/>
    );
  }

  return (
    <Route path={props.path} render={() => returnedComponent} />
  );
}

export default PrivateRoute;
