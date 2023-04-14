<template>
    <div>
      <h1>To Do List</h1>
      <form @submit.prevent="addTask">
        <input type="text" v-model="newTask">
        <button type="submit">Add Task</button>
      </form>
      <ul>
        <li v-for="(task, index) in tasks" :key="index">
          {{ task }}
          <button @click="completeTask(index)">Complete</button>
          <button @click="deleteTask(index, 'tasks')">Delete</button>
        </li>
      </ul>
      <h2>Completed Tasks</h2>
      <ul>
        <li v-for="(task, index) in completedTasks" :key="index">
          {{ task }}
          <button @click="deleteTask(index, 'completedTasks')">Delete</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "ToDoList",
    data() {
      return {
        tasks: ["Example Task 1", "Example Task 2"],
        newTask: "",
        completedTasks: []
      };
    },
    methods: {
      addTask() {
        if (this.newTask.trim() !== "") {
          this.tasks.push(this.newTask);
          this.newTask = "";
        }
      },
      completeTask(index) {
        this.completedTasks.push(this.tasks[index]);
        this.tasks.splice(index, 1);
      },
      deleteTask(index, taskList) {
        if (taskList === "tasks") {
          this.tasks.splice(index, 1);
        } else if (taskList === "completedTasks") {
          this.completedTasks.splice(index, 1);
        }
      }
    }
  };
  </script>
  