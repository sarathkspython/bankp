$(document).ready(function(){
   $("district").change(function(){
      var district_id = $(this).val();
      var url = "/get-states/?district_id="+district_id;
      $.get(url, function(data, status){
           $("#branch").html(data);
      });
   });
});

$(document).ready(function(){
   $("branch").change(function(){
      var branch_id = $(this).val();
      var url = "/get-citys/?branch_id="+branch_id;
      $.get(url, function(data, status){
           $("#city").html(data);
      });
   });
});