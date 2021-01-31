<template>
  <div class="projectContainer">
    <bNav activeTab="project"></bNav>
    <div class="b-intro">
      <div class="b-title">
        <div class="b-h1">项目案例</div>
        <div class="b-h2">PROJECT</div>
      </div>
      <div class="project-container-index">
        <div v-for="(item, index) in list" v-bind:key="index">
          <div class="project-item">
            <img :src="item.fields.image" />
            <div class="project-name">{{ item.fields.name }}</div>
          </div>
        </div>
      </div>

      <el-pagination
        background
        layout="prev, pager, next"
        @current-change="page_change"
        :current-page="currentPage"
        :page-size="pageSize"
        :total="total_count"
      ></el-pagination>
    </div>
    <myfooter></myfooter>
  </div>
</template>
<script>
import bNav from "@/components/nav.vue";
import myfooter from "@/components/footer.vue";
export default {
  components: {
    bNav,
    myfooter,
  },
  name: "project",
  data: function () {
    return {
      list: [],
      load_project_url: "/api/load_project",
      currentPage: 1,
      pageSize: 10,
      total_count: 0,
    };
  },
  created() {
    this.load_project();
  },
  methods: {
    page_change(currentPage) {
      console.log("currentPage", currentPage);
      this.currentPage = currentPage;
      this.load_project();
    },
    load_project() {
      var _this = this;
      let data = {
        offset: _this.pageSize * (_this.currentPage - 1),
        limit: _this.pageSize,
      };
      _this.$axios
        .get(_this.load_project_url, { params: data }) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res);
          _this.list = res.data.objects;
          console.log(_this.list);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style>
template {
  display: flex;
  width: 100%;
  justify-content: flex-start;
}
.b-logo {
  width: 100px;
  height: 75px;
}
.b-h1 {
  font-size: 25px;
  font-family: "microsoft yahei";
}

.b-h2 {
  font-size: 15px;
  font-weight: bold;
  color: rgb(156, 156, 156);
}

#b-nav {
  display: flex;
  width: 1050px;
  height: 85px;
  align-items: center;
  justify-content: space-between;
}
.active div {
  color: red;
}

.b-intro {
  margin-top: 80px;
  width: 1200px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.project-container-index {
  display: flex;
  flex-wrap: wrap;
  justify-content: start;
}
.project-item {
  width: 355px;
  height: 436px;
  border: solid 1px rgb(207, 207, 207);
  margin-bottom: 20px;
  margin-right: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

.project-item:hover{
  border: solid 1px rgb(207, 4, 4);
  cursor: pointer;
}

.project-item img {
  width: 355px;
  height: 355px;
}

.project-name {
  text-align: center;
}
.projectContainer{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
