<template>
  <div id="contact">
  <bNav activeTab='contact'></bNav>
  <div class="contact-content">
    <div class="amap-wrapper">
      <el-amap :center="center" :zoom="zoom" class="amap-box" :vid="'amap-vue'">
        <el-amap-marker :position="[121.28359058574677, 31.100181703788156]" :icon="icon"></el-amap-marker>
      </el-amap>
    </div>
    <div class="contact-right">
      <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604254411587&di=8037e0d270541834430708873374cf5c&imgtype=0&src=http%3A%2F%2Fhiphotos.baidu.com%2Flbsugc%2Fpic%2Fitem%2F42166d224f4a20a47accf17896529822730ed0bb.jpg">
      <div class="contact-item">地址：上海市松江区泗砖路600号A座</div>
      <div class="contact-item">电话：400-8827-567</div>
      <div class="contact-item">邮箱：tgxf@hotmail.com</div>
      <div class="contact-item">微信号：shtgxf</div>
      <div class="contact-title">国内业务</div>
      <div class="contact-item">黄经理：13321975678</div>
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
  name: "contact",
  data: function () {
    return {
      input: null,
      center: [121.28359058574677, 31.100181703788156],
      zoom: 17,
    };
  },
  created() {
  },
  methods: {}
};
</script>

<style>
.amap-box{
  width: 500px;
  height: 500px;
  margin-right: 20px;
}
#contact{
  display: flex;
  flex-direction: column;
  align-items: center;
}

.contact-content{
  margin-top: 40px;
  width: 1050px;
  height: 500px;
  display: flex;
}

.contact-right{
  width: 500px;
}

.contact-right img{
  width: 500px;
  height: 300px;
}

.contact-title{
  margin-top: 50px;
  font-size: 19px;
}
</style>