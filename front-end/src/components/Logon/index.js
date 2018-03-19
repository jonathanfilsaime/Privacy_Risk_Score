import React, { Component } from 'react';
import { Field, reduxForm, SubmissionError, formValueSelector } from 'redux-form'
import { connect } from 'react-redux';
import RenderField from '../RenderField';
import { Redirect } from 'react-router-dom'
import { loginAction } from './actions';

import './styles.css';

const required = value => (value ? undefined : 'Required');
export const minLength = value =>
  value && value.length < 8 ? `Must be 8 characters or more` : undefined
const email = value =>
  value && !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value) ?
  'Invalid email address' : undefined

class Login extends Component {
  constructor(props) {
    super(props);

    this.mySubmit = this.mySubmit.bind(this);
  }

  mySubmit() {
    return this.props.loginAction(this.props.formValues);
  }

  render() {
    const { handleSubmit, error } = this.props;
    const { from } = this.props.location.state || { from: { pathname: '/' } }

    if (this.props.user.loggedIn){
      return (
       <Redirect to={from}/>
     );
    }

    return (
      <form onSubmit={handleSubmit(this.mySubmit)} className="login">
        <div>
          <div>Email</div>
          <div>
            <Field name="email" component={RenderField} type="text" placeholder="email" validate={[required, email]}/>
          </div>
          <div>Password</div>
          <div>
            <Field name="password" component={RenderField} type="password" placeholder="password" validate={[required, minLength]}/>
          </div>
        </div>
        <div>{ error }</div>
        <button type="submit">Submit</button>
      </form>
    );
  }
}

const selector = formValueSelector('selectingFormValues')

const mapStateToProps = (state) => {
  if( state.form.login ) {
    return {
      user: state.user,
      formValues: state.form.login.values,
      email: selector(state, 'email')
    }
  } else {
    return {
      user: state.user
    }
  }

};

Login = connect(
  mapStateToProps,
  { loginAction }
)(Login);

export default reduxForm({
  form: 'login'
})(Login);
