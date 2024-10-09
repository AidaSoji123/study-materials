// src/redux/Store.js
import { createStore } from 'redux';
import todoReducer from './TodoReducer';  // Correct the import path

const store = createStore(todoReducer);

export default store;
