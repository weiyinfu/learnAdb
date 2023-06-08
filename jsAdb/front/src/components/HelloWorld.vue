<script setup>
import { ref } from 'vue'
import {Home as IconHome} from "@icon-park/vue-next";

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
  <div class="Hello">
    <icon-home :size="40"></icon-home>
    <h1>{{ msg }}</h1>

    <p>
      Recommended IDE setup:
      <a href="https://code.visualstudio.com/" target="_blank">VS Code</a>
      +
      <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
    </p>

    <p>
      <a href="https://vitejs.dev/guide/features.html" target="_blank">
        Vite Documentation
      </a>
      |
      <a href="https://v3.vuejs.org/" target="_blank">Vue 3 Documentation</a>
    </p>

    <button type="button" @click="count++">count is: {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test hot module replacement.
    </p>
  </div>
</template>


<style>
a {
  color: #42b983;
}

.Hello {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>
