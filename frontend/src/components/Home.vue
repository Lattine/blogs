/* eslint-disable */
<template>
  <div>
    <div>
      <el-card class="m-card" v-for="(item, index) in items" :key="index">
        <div slot="header">
          <span class="title">{{ item.title }}</span>
        </div>
        <div>{{ item.body }}</div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  components: {},
  data () {
    return {
      items: [],
      posts: {}
    }
  },
  created () {
    this.getPosts()
  },
  methods: {
    getPosts () {
      const path = '/posts'
      this.$axios.get(path)
        .then(response => {
          this.posts = response.data
          this.items = this.posts.items
          console.log(this.posts)
        })
        .catch(error => {
        // eslint-disable-next-line
          console.error(error);
        })
    }
  },
  // 当查询参数 page 或 per_page 变化后重新加载数据
  beforeRouteUpdate (to, from, next) {
    // 注意：要先执行 next() 不然 this.$route.query 还是之前的
    next()
    this.getPosts()
  }

}
</script>

<style scoped>
.m-card {
  margin-bottom: 16px;
}
.title {
  font-size: 17px;
  font-weight: 600;
}
</style>
