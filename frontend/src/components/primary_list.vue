<template>
  <div class="container">
    <table class="table">
      <thead>
        <tr>
          <th>Item</th>
          <th>Completed</th>
          <th>Date Added</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr class="active" v-for="item in items" v-bind:key="item.id">
          <td>{{ item.text }}</td>
          <td>
            <div class="form-group">
              <label class="form-checkbox">
                <input type="checkbox" v-model="item.completed" v-on:change="complete(item)">
                <i class="form-icon"></i>
              </label>
            </div>
          </td>
          <td>{{ item.added_date.toLocaleString() }}</td>
          <td>
            <a href="" v-on:click.prevent="remove(item)">
              <i class="icon icon-delete"></i>
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="input-group">
      <input
        type="text"
        class="form-input"
        placeholder="To do ..."
        v-model="text_field"
        v-on:keyup.enter="add_new()">
      <button
        class="btn btn-primary input-group-btn"
        v-on:click.prevent="add_new()"
        >Add
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'primarylist',
  props: ['url'],
  data: function() {
    return {
      items: [],
      text_field: null
    }
  },
  methods: {
    load_list: function() {
      let self = this;
      axios.get(this.url).then(function(response){
        let items = response.data;
        items = items.map(function(item) {
          item.added_date = new Date(item.added_date).toLocaleString()
          return item
        });

        self.items = items;
      }).catch(function() {
        // do nothing?
      });
    },
    complete: function(item) {
      axios.put(
        `${this.url}${item.id}/`,
        item
      ).catch(function(){
        // do nothing?
      })
    },
    remove: function(item){
      let self = this;
      axios.delete(
        `${this.url}${item.id}/`
      ).then(function(){
        self.items = self.items.filter(function(val) {
          if (val.id !== item.id) {
            return item
          }
        })
      }).catch(function(){
        // do nothing?
      })
    },
    add_new: function() {
      let self = this;
      axios.post(
        this.url,
        {'text': self.text_field}
      ).then(function(response){
        let item = response.data;
        item.added_date = new Date(item.added_date).toLocaleString();
        self.items.push(item);
        self.items.sort((x,y) => x.added_date < y.added_date);
        self.text_field = null;
      }).catch(function(){
        // do nothing?
      })
    }
  },
  created: function() {
    this.load_list();
  }
}
</script>

<style>
  table {
    margin-bottom: 20px;
  }
</style>
