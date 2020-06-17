<template lang="pug">
extends ./annotation.pug

block annotation-area
  div.card
    header.card-header
      div.card-header-title.has-background-royalblue
        div.field.is-grouped.is-grouped-multiline
          div.control(v-for="label in labels")
            div.tags.has-addons
              a.tag.is-medium(
                v-shortkey.once="replaceNull(shortcutKey(label))"
                v-bind:style="{ \
                  color: label.text_color, \
                  backgroundColor: label.background_color \
                }"
                v-on:click="annotate(label.id)"
                v-on:shortkey="annotate(label.id)"
              ) {{ label.text }}
              span.tag.is-medium
                kbd {{ shortcutKey(label) | simpleShortcut }}

    div.card-content
      div.content.scrollable(v-if="docs[pageNumber] && annotations[pageNumber]", ref="textbox")
        annotator(
          v-bind:labels="labels"
          v-bind:entity-positions="annotations[pageNumber]"
          v-bind:search-query="searchQuery"
          v-bind:text="docs[pageNumber].text"
          v-on:remove-label="removeLabel"
          v-on:add-label="addLabel"
          ref="annotator"
          )


block ner-area
  h1 Test Against NER Model
  select.custom-select
    option(selected='') Select NER Model
    option(value='1') en_core_web_sm
    option(value='2') Custom 1
    option(value='3') Custom 2


  div.card
    header.card-header
      div.card-header-title.has-background-royalblue
        div.field.is-grouped.is-grouped-multiline
          div.control(v-for="label in labels")
            div.tags.has-addons
              a.tag.is-medium(
                v-shortkey.once="replaceNull(shortcutKey(label))"
                v-bind:style="{ \
                  color: label.text_color, \
                  backgroundColor: label.background_color \
                }"
                v-on:click="annotate(label.id)"
                v-on:shortkey="annotate(label.id)"
              ) {{ label.text }}
              span.tag.is-medium
                kbd {{ shortcutKey(label) | simpleShortcut }}

    div.card-content
      div.content.scrollable(v-if="docs[pageNumber] && annotations[pageNumber]", ref="textbox")
        annotator(
          v-bind:labels="labels"
          v-bind:entity-positions="annotations[pageNumber]"
          v-bind:search-query="searchQuery"
          v-bind:text="docs[pageNumber].text"
          v-on:remove-label="removeLabel"
          v-on:add-label="addLabel"
          ref="annotator"
          )
</template>

<style scoped>
.card-header-title {
  padding: 1.5rem;
}
</style>

<script>
import annotationMixin from './annotationMixin';
import Annotator from './annotator.vue';
import HTTP from './http';
import { simpleShortcut } from './filter';

export default {
  filters: { simpleShortcut },

  components: { Annotator },

  mixins: [annotationMixin],

  methods: {
    annotate(labelId) {
      this.$refs.annotator.addLabel(labelId);
    },

    addLabel(annotation) {
      const docId = this.docs[this.pageNumber].id;
      HTTP.post(`docs/${docId}/annotations`, annotation).then((response) => {
        this.annotations[this.pageNumber].push(response.data);
      });
    },

    async submit() {
      if (this.picked == "active") {
        this.url = `docs?q=${this.searchQuery}&seq_annotations__isnull=${true}&offset=${this.offset}&ordering=${this.ordering}`;
      } else if (this.picked == "completed") {
        this.url = `docs?q=${this.searchQuery}&seq_annotations__isnull=${false}&offset=${this.offset}&ordering=${this.ordering}&annotations_approved_by_id_isnull=${true}`;
      } else if (this.picked == "approved") {
        this.url = `docs?q=${this.searchQuery}&offset=${this.offset}&ordering=${this.ordering}&annotations_approved_by_id_isnull=${false}`;
      } else {
        this.url = `docs?q=${this.searchQuery}&offset=${this.offset}&ordering=${this.ordering}`;
      }

      await this.search();
      this.pageNumber = 0;
    },
  },
};
</script>
