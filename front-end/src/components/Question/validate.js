const validate = (values, props) => {
  const errors = {};

  if(!values[props.id]){
    errors[props.id] = 'required';
  }

  return errors;
};

export default validate;
