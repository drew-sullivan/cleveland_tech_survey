$(document).ready(function() {
    checkBoxFields = ['tech_roles',
                      'how_you_learned_to_code',
                      'primary_programming_languages_used_at_work',
                      'primary_database_technologies_used_at_work',
                      'primary_platforms_used_at_work',
                      'primary_development_environments_used_at_work',
                      'primary_version_control_systems_used_at_work',
                      'what_you_value_most_in_compensation',
                      'how_you_found_your_current_job',
                      'most_annoying_work_issue',
                      'favorite_office_perk',
                      'what_keeps_you_in_cleveland'];
    $.each(checkBoxFields, function(i, val) {
        $("#" + val).removeClass('form-control');
    });
    $('#myTab').tabCollapse();
});




