import { createStore } from 'redux';

// Initial state
const initialState = {
  counter: 0,
};

// Reducer function
const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, counter: state.counter + 1 };
    case 'DECREMENT':
      return { ...state, counter: state.counter - 1 };
    default:
      return state;
  }
};

// Create the store
const store = createStore(counterReducer);

// Export the store
export default store;
