import { handleAction } from 'redux-actions';
import { GET_DASHBOARD } from './actions';

const defaultState = [];

const dashboardReducer = handleAction(GET_DASHBOARD, (state, action) => {
  return action.payload.data;
}, defaultState);

export default dashboardReducer;
