import { combineReducers } from 'redux';

import { reducer as formReducer } from 'redux-form';
import dashboardReducer from '../components/Dashboard/reducer';
import surveyReducer from '../components/Quiz/reducer';
import scoreReducer from '../components/Score/reducer';
import loginReducer from '../components/Logon/reducer';

const rootReducer = combineReducers({
  dashboard: dashboardReducer,
  form: formReducer,
  user: loginReducer,
  score: scoreReducer,
  survey: surveyReducer
});

export default rootReducer;
