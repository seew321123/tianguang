<template>
  <div class="productContainer">
    <bNav activeTab="product"></bNav>
    <div class="b-intro">
      <div class="b-title">
        <div class="b-h1">产品中心</div>
        <div class="b-h2">PRODUCT</div>
      </div>
      <div class="product-container-index">
        <div v-for="(item, index) in list" v-bind:key="index">
          <div class="product-item" @click="goDetail(item.pk)">
            <img :src="item.fields.image" />
            <div class="product-name">{{ item.fields.name }}</div>
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
  name: "product",
  data: function () {
    return {
      list: [],
      load_product_url: "/api/load_product",
      currentPage: 1,
      pageSize: 10,
      total_count: 0,
    };
  },
  created() {
    this.load_product();
  },
  methods: {
    page_change(currentPage) {
      console.log("currentPage", currentPage);
      this.currentPage = currentPage;
      this.load_product();
    },
    load_product() {
      var _this = this;
      let data = {
        offset: _this.pageSize * (_this.currentPage - 1),
        limit: _this.pageSize,
      };
      _this.$axios
        .get(_this.load_product_url, { params: data }) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res);
          _this.list = res.data.objects;
          console.log(_this.list);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    goDetail(pk){
      console.log('goDetail=>pk', pk)
      this.$router.push({
      path: '/productdetail',
      // name: 'mallList',
      query: {
        pk: pk
      }
      })
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

.product-container-index {
  display: flex;
  flex-wrap: wrap;
  justify-content: start;
}
.product-item {
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

.product-item:hover{
  border: solid 1px rgb(207, 4, 4);
  cursor: pointer;
}

.product-item img {
  width: 355px;
  height: 355px;
}

.product-name {
  text-align: center;
}
.productContainer{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
