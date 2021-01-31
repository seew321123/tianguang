<template>
  <div id="index">
  <bNav activeTab='index'></bNav>
    <el-carousel class="b-scroll-container" indicator-position="outside">
      <el-carousel-item
        class="lunbo-box-item"
        v-for="(item,index) in scroll_list"
        :key="index"
      >
        <img :src="item.fields.image" class="lunbotu" alt="轮播图">
      </el-carousel-item>
    </el-carousel>
    <intro></intro>
    <product></product>
    <news></news>
    <myfooter></myfooter>
  </div>
</template>

<script>
import bNav from "@/components/nav.vue";
import intro from "@/components/intro.vue";
import product from "@/components/product.vue";
import news from "@/components/news.vue";
import myfooter from "@/components/footer.vue";
export default {
  components: {
    intro,
    bNav,
    product,
    news,
    myfooter,
  },
  name: "index",
  data: function () {
    return {
      input: null,
      scroll_list: [],
      load_scroll_url: "/api/load_scroll",
      category_list: [],
      product_list:[],
      get_all_category_url: "/api/get_all_category",
      load_product_url: "/api/load_product",
    };
  },
  created() {
    this.load_scroll()
  },
  methods: {
    load_scroll() {
      var _this = this;
      let data = {
        offset: 0,
        limit: 1000,
      };
      _this.$axios
        .get(_this.load_scroll_url, { params: data }) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res)
          _this.scroll_list = res.data.objects;
          console.log(_this.scroll_list);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style>
#index {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
  .lunbo-box-item, .lunbo-box-item img{
    width:100%;
    height:590px !important;
  }
  .b-scroll-container{
    width:100%;
    height:590px;
  }

</style>