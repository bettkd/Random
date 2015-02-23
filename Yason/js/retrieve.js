(function() {
  var url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults=15&playlistId=UUekTpzKodObpOcmvVCFUvTw&key=AIzaSyCZT5sXBrdsnZ4RMt5r1w6ITaGrGM23A_E";
  var title;
  var videoId;
  var description = [];
  var channelTitle;
  var publishedAt;
  $.getJSON(url,
      function(response){
          
          for (var i = 0; i < response.items.length; i++) {
            title = response.items[i].snippet.title;
            description[i] = response.items[i].snippet.description;
            channelTitle = response.items[i].snippet.channelTitle;
            videoId = response.items[i].snippet.resourceId.videoId;
            publishedAt = response.items[i].snippet.publishedAt;

            //document.write("<h3>" + channelTitle + "</h3><ul>");
            //document.write("<li><b>" + title + "</b></li>");
            //document.write("<li><i>" + description[i] + "</i></li>");
            //document.write("<li> <a href = \"https://www.youtube.com/watch?v=" + videoId + "\">Link </a>&nbsp-&nbsp");
            //document.write("Published at: " + publishedAt + "</li></ul><hr>");

            //return title;
          };
      document.getElementById("demo").innerHTML = title + "<hr>";
  });

   
})();