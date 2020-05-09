import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
const baseUrl = window.location.href.split('/').slice(4, 6).join('/');
const HTTP = axios.create({
  baseURL: `/doccano/v1/${baseUrl}`,
});

export const defaultHttpClient = axios.create();
export default HTTP;
