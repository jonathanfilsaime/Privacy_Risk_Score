import { createAction, handleAction } from 'redux-actions';
import axios from 'axios';

export const GET_SCORE = 'GET_SCORE';

export const getScoreAction = createAction(GET_SCORE, function() {
  // console.log('localStorage is ', localStorage.getItem('PRS-id'));
  const request = axios.post('http://privacy-risks-core.appspot.com/score',
    [parseInt(localStorage.getItem('PRS-id'))]
  );
  return request;
});

export default getScoreAction;
