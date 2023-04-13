<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <img alt="quiz logo" src="./assets/quiz.jpg" style="width: 25%; height: auto;">
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <QuizComp/>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import QuizComp from './components/QuizComp.vue'

export default {
  name: 'App',
  components: {
    QuizComp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
