<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{msg}}</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    get_message () {
      const path = 'http://localhost:5000/api/ping'
      axios
        .get(path)
        .then(res => {
          this.msg = res.data
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        })
    }
  },
  created () {
    this.get_message()
  }
}
</script>
