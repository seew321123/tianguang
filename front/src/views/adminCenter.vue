<template>
  <div class="container">
    <el-col :span="2">
      <el-menu
        style="height:900px;"
        default-active="1"
        class="el-menu-vertical-demo"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        @select="handleSelect"
      >
        <el-menu-item index="1">
          <i class="el-icon-menu"></i>
          <span slot="title">产品管理</span>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">分类管理</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-menu"></i>
          <span slot="title">滚动图管理</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-menu"></i>
          <span slot="title">配置管理</span>
        </el-menu-item>
        <el-menu-item index="5">
          <i class="el-icon-menu"></i>
          <span slot="title">资讯管理</span>
        </el-menu-item>
        <el-menu-item index="6">
          <i class="el-icon-menu"></i>
          <span slot="title">业绩管理</span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <div>
      <div id="nav" style="background-color:#545c64;color:white;width:100%">
        <router-link to="/">Home</router-link>|
        <router-link to="/admincenter">管理中心</router-link>|
        <router-link to="/index">商城首页</router-link>
      </div>
      <div class="pageContainer" v-if="activeIndex==1">
        <Admin></Admin>
      </div>
      <div class="pageContainer" v-if="activeIndex==2">
        <categoryAdmin></categoryAdmin>
      </div>
      <div class="pageContainer" v-if="activeIndex==3">
        <scrollAdmin></scrollAdmin>
      </div>
      <div class="pageContainer" v-if="activeIndex==4">
        <configAdmin></configAdmin>
      </div>
      <div class="pageContainer" v-if="activeIndex==5">
        <adminNews></adminNews>
      </div>
        <div class="pageContainer" v-if="activeIndex==6">
        <projectAdmin></projectAdmin>
      </div>
    </div>
  </div>
</template>

<script>
import Admin from "./Admin.vue";
import categoryAdmin from "./categoryAdmin.vue";
import projectAdmin from "./projectAdmin.vue";
import scrollAdmin from "./scrollAdmin.vue";
import configAdmin from "./configAdmin.vue";
import adminNews from "./adminNews.vue";
export default {
  components: {
    Admin,
    categoryAdmin,
    projectAdmin,
    scrollAdmin,
    configAdmin,
    adminNews,
  },
  data: function () {
    return {
      activeIndex: "1",
    };
  },
  methods: {
    handleSelect(index) {
      console.log("index=>", index);
      this.activeIndex = index;
    },
  },
};
</script>

<style>
.container {
  display: flex;
}
.pageContainer {
  margin-top: 20px;
  margin-left: 20px;
}
</style>