var topologyData = null;

url =  'http://localhost:8000/mytopology/data/'

$.ajax({
  url: url,
  async: false,
  dataType: 'json',
  success: function (json) {   
    assignVariable(json);
  }
});

function assignVariable(data) {
  topologyData = data;
}
