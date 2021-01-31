<template>
  <div class="productContainer">
    <bNav activeTab="product"></bNav>
    <div class="big-image" style="width: 100%;">
      <img style="width: 100%;" src="http://qn22vegbe.hn-bkt.clouddn.com/5f23dcb0c01d5.jpg?e=1610851385&token=VxETw_LcNTYG8nciV9HvHAIYMMwZxssBQIt4rwKW:MDmVSUiPzuanFiimlkJAww0oXH8=" alt="图片加载失败">
    </div>
    <div class="b-intro">
      <div class="b-title">
        <div class="b-h1">产品详情</div>
        <div class="b-h2">PRODUCT-DETAIL</div>
      </div>
      <div class="product-container-detail">
        <div class="product-detail-item">
          <img :src="item.fields.image" />
        </div>
        <div class="product-detail-right" style="color: rgb(126, 122, 122);">
          <h1> 产品名称:{{ item.fields.name }}</h1>
          <h2>
            产品分类：{{ item.fields.category }}
          </h2>
          <h2>
            产品价格：{{ item.fields.price / 100 }}元
          </h2>
          <div class="buttonGroup">
            <div class="button-item" data-key="phone">
              电话联系
              <div class="phone">13321975678</div>
            </div>
            <div class="button-item" data-key="wechat">
              微信沟通
              <div class="wechat">
                <img src="http://qn22vegbe.hn-bkt.clouddn.com/gh_0bc07e484682_258.jpg" alt="">
              </div>
            </div>
          </div>
        </div>
        <div>

        </div>
      </div>
      <div class="product-detail-desc" v-html="item.fields.description">
      </div>
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
    name: "productdetail",
    data: function () {
      return {
        item: null,
        product_detail_url: "/api/product_detail",
        currentPage: 1,
        pageSize: 10,
        total_count: 0,
      };
    },
    created() {
      console.log('params', this.$route.query)
      this.load_product();
    },
    methods: {
      load_product() {
        var _this = this;
        let pk = _this.$route.query.pk
        let data = {
          pk: pk
        }
        _this.$axios
          .get(_this.product_detail_url, {
            params: data
          }) // 还可以直接把参数拼接在url后边
          .then(function (res) {
            console.log("res", res);
            _this.item = res.data.object;
            console.log(_this.item);
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

  .product-container-detail {
    display: flex;
    flex-direction: row;
    justify-content: start;
    border: solid 1px rgb(207, 207, 207);
  }
  .product-detail-desc *{
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .product-detail-item {
    width: 355px;
    height: 436px;
    /* border: solid 1px rgb(207, 207, 207); */
    margin-bottom: 20px;
    margin-right: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    overflow: hidden;
  }

  .product-item:hover {
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

  .productContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .buttonGroup{
    display: flex;
  }
  .button-item{
    position: relative;
    font-size: 24px;
    width: 150px;
    height: 60px;
    line-height: 60px;
    text-align: center;
    color: rgb(207, 4, 4);
    border: solid 1px rgb(207, 4, 4);
    border-radius: 10px;
    margin: 0 20px;
    transition: ease-in-out 0.3s;
    cursor: pointer;
  }
  .phone{
    position: absolute;
    display: none;
    transition: ease-in-out 1s;
  }
  .wechat{
    position: absolute;
    display: none;
    transition: ease-in-out 1s;
  }
  .button-item:hover{
    background-color: rgb(207, 4, 4);
    color: white;
  }
  .button-item[data-key="phone"]:hover .phone{
    opacity: 1;
    color: rgb(207, 4, 4);
    display: block;
  }
  .button-item[data-key="wechat"]:hover .wechat{
    opacity: 1;
    color: rgb(207, 4, 4);
    display: block;
  }
  .wechat img{
    width: 200px;
    height: 200px;
  }
</style>