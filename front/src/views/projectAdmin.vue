<template>
  <div class="about">
    <header class="header">
      <el-button class="newButton" style="height:40px;" @click="newproject">新建</el-button>
    </header>
    <div v-for="(item,index) in list" v-bind:key="index">
      <div class="project_th" v-if="index==0">
        <div style="width:150px;">业绩ID</div>
        <div style="width:300px;">业绩名称</div>
        <div style="width:300px;">业绩图片</div>
        <div style="width:150px;">操作</div>
      </div>
      <div class="project_container">
        <div style="width:150px;">{{ item.pk }}</div>
        <div style="width:300px;">{{ item.fields.name }}</div>
        <div style="width:300px;" class="image_container">
          <img :src="item.fields.image" />
        </div>
        <div style="width:150px;">
          <el-button
            type="primary"
            @click="editproject(item)"
            style="height:40px;"
            icon="el-icon-edit"
            circle
          ></el-button>
          <el-button
            type="danger"
            @click="delete_project(item.pk)"
            style="height:40px;"
            icon="el-icon-delete"
            circle
          ></el-button>
        </div>
      </div>
    </div>
    <el-pagination background layout="prev, pager, next" @current-change="page_change" :current-page="currentPage" :page-size="pageSize" :total="total_count"></el-pagination>
    <el-dialog title="新建分类" :visible.sync="show_form" @close="hideForm">
      <el-form ref="form" label-width="80px">
        <el-form-item label="分类名称">
          <el-input v-model="formData.name"></el-input>
        </el-form-item>
        <el-form-item label="分类图片">
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
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>
        <el-form-item>
          <el-button @click="upload_project">确认提交</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>

export default {
  name: "projectAdmin",
  data: function () {
    return {
      currentPage: 1,
      pageSize: 10,
      total_count: 0,
      load_project_url: "/api/load_project",
      receive_image_url: "/api/receive_image",
      upload_project_url: "/api/add_project/",
      delete_project_url: "/api/delete_project/",
      edit_project_url: "/api/edit_project/",
      list: [],
      show_form: false,
      fileList: [],
      formData: {
        name: null,
        image: null,
      },
      defaultFormData: {
        name: "文本",
        image: null,
      },
      currentItem: null,
    };
  },
  created() {
    console.log("111");
    this.load_project();
  },
  methods: {
    page_change(currentPage){
      console.log('currentPage',currentPage)
      this.currentPage = currentPage
      this.load_project()
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
          console.log("res", res)
          _this.list = res.data.objects;
          _this.total_count = res.data.total_count;
          console.log(_this.list);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    showForm() {
      this.show_form = true;
      if (this.formData.image) {
        this.fileList.push({
          name: this.formData.image,
          url: this.formData.image,
          uid: new Date().getTime(),
          status: "success",
        });
      }
    },
    hideForm() {
      this.show_form = false;
      this.currentItem = null;
      this.formData = {};
      this.fileList = [];
      console.log("完成formdata清除=>", this.formData);
    },
    newproject() {
      this.formData = JSON.parse(JSON.stringify(this.defaultFormData));
      this.showForm();
    },
    editproject(e) {
      this.currentItem = e;
      this.formData = {
        name: e.fields.name,
        image: e.fields.image,
      };
      this.showForm();
    },
    upload_image(response, file, fileList) {
      //这里要做的两件事，
      //1.获取后端保存图片的路径
      //2.将data中的formData.image改为此路径
      console.log("response", response);
      this.formData.image = response.response.file_path;
      console.log("this.formData", this.formData);
    },
    upload_project() {
      var _this = this;

      var params = new URLSearchParams();
      params.append("name", _this.formData.name); //你要传给后台的参数值 key/value
      params.append("image", _this.formData.image);
      if (this.currentItem) {
        params.append("pk", _this.currentItem.pk);
        _this.$axios
          .post(_this.edit_project_url, params) // 还可以直接把参数拼接在url后边
          .then(function (res) {
            console.log("res", res);
          })
          .catch(function (error) {
            console.log(error);
          });
      } else {
        _this.$axios
          .post(_this.upload_project_url, params) // 还可以直接把参数拼接在url后边
          .then(function (res) {
            console.log("res", res);
          })
          .catch(function (error) {
            console.log(error);
          });
      }
      _this.hideForm();
      _this.load_project();
    },
    delete_project(e) {
      var _this = this;
      let data = {
        pk: e,
      };
      _this.$axios
        .get(_this.delete_project_url, { params: data }) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res);
        })
        .catch(function (error) {
          console.log(error);
        });
      _this.load_project();
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
form {
  width: 600px;
}
header {
  display: flex;
}
header * {
  flex-grow: 0;
  max-width: 100%;
  flex-basis: auto;
}

.project_container {
  display: flex;
  width: 900px;
  border-right: 1px solid rgb(199, 199, 199);
}
.project_container > div {
  padding: 5px;
  border-left: 1px solid rgb(199, 199, 199);
  border-bottom: 1px solid rgb(199, 199, 199);
}

.image_container > img {
  width: 60px;
  height: 60px;
}
.newButton {
  margin-left: auto !important;
}
.project_th {
  display: flex;
  width: 900px;
  border-right: 1px solid rgb(199, 199, 199);
  border-top: 1px solid rgb(199, 199, 199);
}
.project_th > div {
  padding: 5px;
  border-left: 1px solid rgb(199, 199, 199);
  border-bottom: 1px solid rgb(199, 199, 199);
}
</style>
