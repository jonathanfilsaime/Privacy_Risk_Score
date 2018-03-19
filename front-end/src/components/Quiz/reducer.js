import { handleAction } from 'redux-actions';
import { GET_SURVEY } from './actions';

const defaultState = [];

const surveyReducer = handleAction(GET_SURVEY, (state, action) => {
  return action.payload.data;
}, defaultState);

export default surveyReducer;
