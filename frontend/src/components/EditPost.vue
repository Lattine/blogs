<template>
  <div>
    <el-card class="m-card">
      <div>
        <el-input placeholder="标题" v-model="title"></el-input>
      </div>
      <div style="margin-top:10px;">
        <el-button type="primary" size="medium" @click="onSave">保存</el-button>
      </div>
    </el-card>
    <mavon-editor class="mavon-editor" v-model="body"/>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: '',
      body: ''
    }
  },
  methods: {
    // 保存
    onSave () {
      const path = '/posts'
      const payload = {
        title: this.title,
        body: this.body
      }
      console.log(payload)
      this.$axios.post(path, payload)
        .then((response) => {
          // handle success
          this.$toasted.success('Congratulations, you are now create a post !', {icon: 'fingerprint'})
          this.$router.push('/')
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    }
  }
}
</script>

<style scoped>
.m-card {
  margin-bottom: 16px;
}
.mavon-editor {
  width: 100vw;
  min-height: 40vh;
}
</style>
