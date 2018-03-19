import { createAction, handleAction } from 'redux-actions';
import axios from 'axios';

export const GET_SURVEY = 'GET_SURVEY';
export const POST_SURVEY_ANSWERS = 'POST_SURVEY_ANSWERS';

export const getSurveyAction = createAction(GET_SURVEY, function() {
  const request = axios.get('http://privacy-risks-core.appspot.com/survey');
  return request;
});

export const postSurveyAnswers = createAction(POST_SURVEY_ANSWERS, function(answers) {

  answers.shift();

  answers = answers.map((answer, index) => {
    return {
      [index]: answer
    }
  })

  const request = axios.post('http://privacy-risks-core.appspot.com/survey', answers);
  return request;
});
