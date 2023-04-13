<template>
    <div class="hello">
      <p>
        Welcome to the QuizApp.
      </p>
      <h3>Please enter a name for the dummy quiz:</h3>
      <form @submit.prevent="submitForm">
        <label>
            Name:
            <input type="text" v-model="name" />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'QuizComp',
    data() {
        return {
            name: 'dummy quiz'
        };
    },
    methods: {
        submitForm() {
            // You can do some action with the submitted data here
            console.log(`Name: ${this.name}`);
            // Clear the input fields after submission
            this.name = '';
        },
    },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  