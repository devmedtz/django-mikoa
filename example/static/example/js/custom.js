$(document).ready(function() {
    $('#region').change(function() {
        var regionID = $(this).val();
        var url = $(this).attr('load-district-url');
        console.log(regionID);
        $.ajax({
            url: url,
            type: 'GET', 
            data: {
                'region_id': regionID
            },
            success: function (data) {
                $('#district').html(data)
            }
        })
    })
})