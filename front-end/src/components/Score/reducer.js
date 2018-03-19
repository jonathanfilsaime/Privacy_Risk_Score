import { handleActions } from 'redux-actions';
import { POST_SURVEY_ANSWERS } from '../Quiz/actions';
import { GET_SCORE } from './actions';

const defaultState = {score: [{score: 0, total: 100, average: 0}], rec: [{category: 0, link: ''}]};

const scoreReducer = handleActions({
  POST_SURVEY_ANSWERS: (state, action) => {
    // console.log('Setting localstorage to ', action.payload.data[1])
    localStorage.setItem('PRS-id', action.payload.data[1]);
    return {...state};
  },
  GET_SCORE: (state, action) => {
    // console.log('using localstorage to get score');
    return {...state, score: action.payload.data[0], rec: action.payload.data[1]};
  }
}, defaultState);

export default scoreReducer;
