import { createAction, handleAction } from 'redux-actions';
import axios from 'axios';

export const GET_DASHBOARD = 'GET_DASHBOARD';

export const getDashboardAction = createAction(GET_DASHBOARD, function() {
  const request = axios.get('http://privacy-risks-core.appspot.com/admin/dashboard');
  return request;
});

export default getDashboardAction;
