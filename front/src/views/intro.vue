<template>
  <div id="intro">
    <bNav activeTab="intro"></bNav>
    <div class="my-intro" v-html="config.aboutUs"></div>
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
  name: "index",
  data: function () {
    return {
      load_config_url: "/api/load_config",
      config: {},
    };
  },
  created() {
    this.load_config();
  },
  methods: {
    load_config() {
      var _this = this;
      _this.$axios
        .get(_this.load_config_url) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res);
          _this.config = res.data.object;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style>

#intro{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.my-intro{
  width:1050px;
}
</style>