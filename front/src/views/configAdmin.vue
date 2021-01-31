<template>
  <div>
    <h3>头部图片</h3>
    <el-upload
      class="upload-demo"
      action="/api/upload_qiniu_image/"
      :limit="1"
      name="image"
      :on-success="upload_image"
      :file-list="fileList"
      list-type="picture"
    >
      <el-button size="small" type="primary">点击上传</el-button>
      <div slot="tip" class="el-upload__tip">
        只能上传jpg/png文件，且不超过500kb
      </div>
    </el-upload>
    <h3>关于我们</h3>
    <quillEditor v-model="config.aboutUs" :options="quillOption" />
    <el-button @click="save_config" style="margin-top:20px;">保存配置</el-button>
  </div>
</template>
<script>
import { quillEditor } from "vue-quill-editor";
import quillConfig from "./quillconfig";
export default {
  components: {
    quillEditor,
  },
  name: "configAdmin",
  data: function () {
    return {
      config: {},
      fileList: [],
      load_config_url: "/api/load_config",
      edit_config_url: "/api/edit_config/",
      quillOption: quillConfig,
    };
  },
  created() {
    console.log("111");
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
          _this.fileList.push({
            name: _this.config.headerImage,
            url: _this.config.headerImage,
            uid: new Date().getTime(),
            status: "success",
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    upload_image(response, file, fileList) {
      //这里要做的两件事，
      //1.获取后端保存图片的路径
      //2.将data中的formData.image改为此路径
      console.log("response", response);
      this.config.headerImage = response.response.file_path;
    },
    save_config() {
      var _this = this;
      var params = new URLSearchParams();
      params.append("headerImage", _this.config.headerImage); //你要传给后台的参数值 key/value
      params.append("aboutUs", _this.config.aboutUs);
      params.append("id", _this.config.id);
      _this.$axios
        .post(_this.edit_config_url, params) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style>
</style>
