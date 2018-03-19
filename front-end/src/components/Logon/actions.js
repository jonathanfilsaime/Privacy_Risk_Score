import axios from 'axios';
import { createAction, handleAction } from 'redux-actions';

export const LOGIN = 'LOGIN';
export const LOGOUT = 'LOGOUT';

const loginAction = createAction(LOGIN, function(formValues) {
  let valid = false;

  if (formValues.email === 'person@usaa.com' && formValues.password === 'password') {
    valid = true;
  }
    
  return valid;
});

const logoutAction = createAction(LOGOUT, function() {
  return {};
});

export { loginAction, logoutAction };
