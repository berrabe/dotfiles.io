static void GENERATED_call(const int call_identifier, struct CommandResultIR *result) {
    switch (call_identifier) {
         case 0:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_rename_workspace(&current_match, result, "to", get_string("new_name"));
#else
           fprintf(stderr, "cmd_rename_workspace(%s, %s)\n", "to", get_string("new_name"));
#endif
             break;
         case 1:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_rename_workspace(&current_match, result, NULL, "to");
#else
           fprintf(stderr, "cmd_rename_workspace(NULL, %s)\n", "to");
#endif
             break;
         case 2:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_rename_workspace(&current_match, result, get_string("old_name"), get_string("new_name"));
#else
           fprintf(stderr, "cmd_rename_workspace(%s, %s)\n", get_string("old_name"), get_string("new_name"));
#endif
             break;
         case 3:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_rename_workspace(&current_match, result, NULL, get_string("new_name"));
#else
           fprintf(stderr, "cmd_rename_workspace(NULL, %s)\n", get_string("new_name"));
#endif
             break;
         case 4:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_workspace_to_output(&current_match, result, get_string("output"));
#else
           fprintf(stderr, "cmd_move_workspace_to_output(%s)\n", get_string("output"));
#endif
             break;
         case 5:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace_number(&current_match, result, get_string("number"), get_string("no_auto_back_and_forth"));
#else
           fprintf(stderr, "cmd_move_con_to_workspace_number(%s, %s)\n", get_string("number"), get_string("no_auto_back_and_forth"));
#endif
             break;
         case 6:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_resize(&current_match, result, get_string("way"), get_string("direction"), get_long("resize_px"), get_long("resize_ppt"));
#else
           fprintf(stderr, "cmd_resize(%s, %s, %ld, %ld)\n", get_string("way"), get_string("direction"), get_long("resize_px"), get_long("resize_ppt"));
#endif
             break;
         case 7:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_resize(&current_match, result, get_string("way"), get_string("direction"), get_long("resize_px"), get_long("resize_ppt"));
#else
           fprintf(stderr, "cmd_resize(%s, %s, %ld, %ld)\n", get_string("way"), get_string("direction"), get_long("resize_px"), get_long("resize_ppt"));
#endif
             break;
         case 8:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_window_to_position(&current_match, result, get_long("coord_x"), get_long("coord_y"));
#else
           fprintf(stderr, "cmd_move_window_to_position(%ld, %ld)\n", get_long("coord_x"), get_long("coord_y"));
#endif
             break;
         case 9:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_window_to_position(&current_match, result, get_long("coord_x"), get_long("coord_y"));
#else
           fprintf(stderr, "cmd_move_window_to_position(%ld, %ld)\n", get_long("coord_x"), get_long("coord_y"));
#endif
             break;
         case 10:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_fullscreen(&current_match, result, "toggle", get_string("mode"));
#else
           fprintf(stderr, "cmd_fullscreen(%s, %s)\n", "toggle", get_string("mode"));
#endif
             break;
         case 11:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_fullscreen(&current_match, result, "toggle", "output");
#else
           fprintf(stderr, "cmd_fullscreen(%s, %s)\n", "toggle", "output");
#endif
             break;
         case 12:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_direction(&current_match, result, get_string("direction"), get_long("pixels"));
#else
           fprintf(stderr, "cmd_move_direction(%s, %ld)\n", get_string("direction"), get_long("pixels"));
#endif
             break;
         case 13:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_direction(&current_match, result, get_string("direction"), get_long("pixels"));
#else
           fprintf(stderr, "cmd_move_direction(%s, %ld)\n", get_string("direction"), get_long("pixels"));
#endif
             break;
         case 14:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_window_to_center(&current_match, result, get_string("method"));
#else
           fprintf(stderr, "cmd_move_window_to_center(%s)\n", get_string("method"));
#endif
             break;
         case 15:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_window_to_mouse(&current_match, result);
#else
           fprintf(stderr, "cmd_move_window_to_mouse()\n");
#endif
             break;
         case 16:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_window_to_mouse(&current_match, result);
#else
           fprintf(stderr, "cmd_move_window_to_mouse()\n");
#endif
             break;
         case 17:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_window_to_mouse(&current_match, result);
#else
           fprintf(stderr, "cmd_move_window_to_mouse()\n");
#endif
             break;
         case 18:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_workspace_number(&current_match, result, get_string("workspace"), get_string("no_auto_back_and_forth"));
#else
           fprintf(stderr, "cmd_workspace_number(%s, %s)\n", get_string("workspace"), get_string("no_auto_back_and_forth"));
#endif
             break;
         case 19:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_fullscreen(&current_match, result, get_string("action"), get_string("mode"));
#else
           fprintf(stderr, "cmd_fullscreen(%s, %s)\n", get_string("action"), get_string("mode"));
#endif
             break;
         case 20:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_fullscreen(&current_match, result, get_string("action"), "output");
#else
           fprintf(stderr, "cmd_fullscreen(%s, %s)\n", get_string("action"), "output");
#endif
             break;
         case 21:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_gaps(&current_match, result, get_string("type"), get_string("scope"), get_string("mode"), get_string("value"));
#else
           fprintf(stderr, "cmd_gaps(%s, %s, %s, %s)\n", get_string("type"), get_string("scope"), get_string("mode"), get_string("value"));
#endif
             break;
         case 22:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_direction(&current_match, result, get_string("direction"), 10);
#else
           fprintf(stderr, "cmd_move_direction(%s, %d)\n", get_string("direction"), 10);
#endif
             break;
         case 23:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_output(&current_match, result, get_string("output"));
#else
           fprintf(stderr, "cmd_move_con_to_output(%s)\n", get_string("output"));
#endif
             break;
         case 24:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace(&current_match, result, get_string("workspace"));
#else
           fprintf(stderr, "cmd_move_con_to_workspace(%s)\n", get_string("workspace"));
#endif
             break;
         case 25:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace(&current_match, result, get_string("workspace"));
#else
           fprintf(stderr, "cmd_move_con_to_workspace(%s)\n", get_string("workspace"));
#endif
             break;
         case 26:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace(&current_match, result, get_string("workspace"));
#else
           fprintf(stderr, "cmd_move_con_to_workspace(%s)\n", get_string("workspace"));
#endif
             break;
         case 27:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace(&current_match, result, get_string("workspace"));
#else
           fprintf(stderr, "cmd_move_con_to_workspace(%s)\n", get_string("workspace"));
#endif
             break;
         case 28:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace(&current_match, result, get_string("workspace"));
#else
           fprintf(stderr, "cmd_move_con_to_workspace(%s)\n", get_string("workspace"));
#endif
             break;
         case 29:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace_back_and_forth(&current_match, result);
#else
           fprintf(stderr, "cmd_move_con_to_workspace_back_and_forth()\n");
#endif
             break;
         case 30:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_workspace_name(&current_match, result, get_string("workspace"), get_string("no_auto_back_and_forth"));
#else
           fprintf(stderr, "cmd_move_con_to_workspace_name(%s, %s)\n", get_string("workspace"), get_string("no_auto_back_and_forth"));
#endif
             break;
         case 31:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_append_layout(&current_match, result, get_string("path"));
#else
           fprintf(stderr, "cmd_append_layout(%s)\n", get_string("path"));
#endif
             break;
         case 32:
             result->next_state = CRITERIA;
#ifndef TEST_PARSER
             cmd_criteria_add(&current_match, result, get_string("ctype"), get_string("cvalue"));
#else
           fprintf(stderr, "cmd_criteria_add(%s, %s)\n", get_string("ctype"), get_string("cvalue"));
#endif
             break;
         case 33:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout_toggle(&current_match, result, get_string("toggle_mode"));
#else
           fprintf(stderr, "cmd_layout_toggle(%s)\n", get_string("toggle_mode"));
#endif
             break;
         case 34:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout_toggle(&current_match, result, get_string("toggle_mode"));
#else
           fprintf(stderr, "cmd_layout_toggle(%s)\n", get_string("toggle_mode"));
#endif
             break;
         case 35:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_resize_set(&current_match, result, get_long("width"), get_string("mode_width"), get_long("height"), get_string("mode_height"));
#else
           fprintf(stderr, "cmd_resize_set(%ld, %s, %ld, %s)\n", get_long("width"), get_string("mode_width"), get_long("height"), get_string("mode_height"));
#endif
             break;
         case 36:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_resize(&current_match, result, get_string("way"), get_string("direction"), get_long("resize_px"), 0);
#else
           fprintf(stderr, "cmd_resize(%s, %s, %ld, %d)\n", get_string("way"), get_string("direction"), get_long("resize_px"), 0);
#endif
             break;
         case 37:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_swap(&current_match, result, get_string("mode"), get_string("arg"));
#else
           fprintf(stderr, "cmd_swap(%s, %s)\n", get_string("mode"), get_string("arg"));
#endif
             break;
         case 38:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_border(&current_match, result, get_string("border_style"), -1);
#else
           fprintf(stderr, "cmd_border(%s, %d)\n", get_string("border_style"), -1);
#endif
             break;
         case 39:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_border(&current_match, result, get_string("border_style"), get_long("border_width"));
#else
           fprintf(stderr, "cmd_border(%s, %ld)\n", get_string("border_style"), get_long("border_width"));
#endif
             break;
         case 40:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_output(&current_match, result, get_string("output"));
#else
           fprintf(stderr, "cmd_focus_output(%s)\n", get_string("output"));
#endif
             break;
         case 41:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_con_to_mark(&current_match, result, get_string("mark"));
#else
           fprintf(stderr, "cmd_move_con_to_mark(%s)\n", get_string("mark"));
#endif
             break;
         case 42:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_resize_set(&current_match, result, get_long("width"), get_string("mode_width"), 0, 0);
#else
           fprintf(stderr, "cmd_resize_set(%ld, %s, %d, %d)\n", get_long("width"), get_string("mode_width"), 0, 0);
#endif
             break;
         case 43:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_title_format(&current_match, result, get_string("format"));
#else
           fprintf(stderr, "cmd_title_format(%s)\n", get_string("format"));
#endif
             break;
         case 44:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_fullscreen(&current_match, result, get_string("action"), "output");
#else
           fprintf(stderr, "cmd_fullscreen(%s, %s)\n", get_string("action"), "output");
#endif
             break;
         case 45:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_scratchpad_show(&current_match, result);
#else
           fprintf(stderr, "cmd_scratchpad_show()\n");
#endif
             break;
         case 46:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_resize(&current_match, result, get_string("way"), get_string("direction"), 10, 10);
#else
           fprintf(stderr, "cmd_resize(%s, %s, %d, %d)\n", get_string("way"), get_string("direction"), 10, 10);
#endif
             break;
         case 47:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_workspace(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_workspace(%s)\n", get_string("direction"));
#endif
             break;
         case 48:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_workspace(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_workspace(%s)\n", get_string("direction"));
#endif
             break;
         case 49:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_workspace(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_workspace(%s)\n", get_string("direction"));
#endif
             break;
         case 50:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_workspace(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_workspace(%s)\n", get_string("direction"));
#endif
             break;
         case 51:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_workspace_back_and_forth(&current_match, result);
#else
           fprintf(stderr, "cmd_workspace_back_and_forth()\n");
#endif
             break;
         case 52:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_workspace_name(&current_match, result, get_string("workspace"), get_string("no_auto_back_and_forth"));
#else
           fprintf(stderr, "cmd_workspace_name(%s, %s)\n", get_string("workspace"), get_string("no_auto_back_and_forth"));
#endif
             break;
         case 53:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_bar(&current_match, result, get_string("bar_type"), get_string("bar_value"), get_string("bar_id"));
#else
           fprintf(stderr, "cmd_bar(%s, %s, %s)\n", get_string("bar_type"), get_string("bar_value"), get_string("bar_id"));
#endif
             break;
         case 54:
             result->next_state = CRITERIA;
#ifndef TEST_PARSER
             cmd_criteria_add(&current_match, result, get_string("ctype"), NULL);
#else
           fprintf(stderr, "cmd_criteria_add(%s, NULL)\n", get_string("ctype"));
#endif
             break;
         case 55:
             result->next_state = CRITERIA;
#ifndef TEST_PARSER
             cmd_criteria_add(&current_match, result, get_string("ctype"), NULL);
#else
           fprintf(stderr, "cmd_criteria_add(%s, NULL)\n", get_string("ctype"));
#endif
             break;
         case 56:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_criteria_match_windows(&current_match, result);
#else
           fprintf(stderr, "cmd_criteria_match_windows()\n");
#endif
             break;
         case 57:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_debuglog(&current_match, result, get_string("argument"));
#else
           fprintf(stderr, "cmd_debuglog(%s)\n", get_string("argument"));
#endif
             break;
         case 58:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_debuglog(&current_match, result, get_string("argument"));
#else
           fprintf(stderr, "cmd_debuglog(%s)\n", get_string("argument"));
#endif
             break;
         case 59:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_debuglog(&current_match, result, get_string("argument"));
#else
           fprintf(stderr, "cmd_debuglog(%s)\n", get_string("argument"));
#endif
             break;
         case 60:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_floating(&current_match, result, get_string("floating"));
#else
           fprintf(stderr, "cmd_floating(%s)\n", get_string("floating"));
#endif
             break;
         case 61:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_floating(&current_match, result, get_string("floating"));
#else
           fprintf(stderr, "cmd_floating(%s)\n", get_string("floating"));
#endif
             break;
         case 62:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_floating(&current_match, result, get_string("floating"));
#else
           fprintf(stderr, "cmd_floating(%s)\n", get_string("floating"));
#endif
             break;
         case 63:
             result->next_state = CRITERIA;
#ifndef TEST_PARSER
             cmd_criteria_init(&current_match, result);
#else
           fprintf(stderr, "cmd_criteria_init()\n");
#endif
             break;
         case 64:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_exit(&current_match, result);
#else
           fprintf(stderr, "cmd_exit()\n");
#endif
             break;
         case 65:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_restart(&current_match, result);
#else
           fprintf(stderr, "cmd_restart()\n");
#endif
             break;
         case 66:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_reload(&current_match, result);
#else
           fprintf(stderr, "cmd_reload()\n");
#endif
             break;
         case 67:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_open(&current_match, result);
#else
           fprintf(stderr, "cmd_open()\n");
#endif
             break;
         case 68:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_border(&current_match, result, get_string("border_style"), 0);
#else
           fprintf(stderr, "cmd_border(%s, %d)\n", get_string("border_style"), 0);
#endif
             break;
         case 69:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_border(&current_match, result, "pixel", 1);
#else
           fprintf(stderr, "cmd_border(%s, %d)\n", "pixel", 1);
#endif
             break;
         case 70:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout(&current_match, result, get_string("layout_mode"));
#else
           fprintf(stderr, "cmd_layout(%s)\n", get_string("layout_mode"));
#endif
             break;
         case 71:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout(&current_match, result, get_string("layout_mode"));
#else
           fprintf(stderr, "cmd_layout(%s)\n", get_string("layout_mode"));
#endif
             break;
         case 72:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout(&current_match, result, get_string("layout_mode"));
#else
           fprintf(stderr, "cmd_layout(%s)\n", get_string("layout_mode"));
#endif
             break;
         case 73:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout(&current_match, result, get_string("layout_mode"));
#else
           fprintf(stderr, "cmd_layout(%s)\n", get_string("layout_mode"));
#endif
             break;
         case 74:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout(&current_match, result, get_string("layout_mode"));
#else
           fprintf(stderr, "cmd_layout(%s)\n", get_string("layout_mode"));
#endif
             break;
         case 75:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_layout(&current_match, result, get_string("layout_mode"));
#else
           fprintf(stderr, "cmd_layout(%s)\n", get_string("layout_mode"));
#endif
             break;
         case 76:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_shmlog(&current_match, result, get_string("argument"));
#else
           fprintf(stderr, "cmd_shmlog(%s)\n", get_string("argument"));
#endif
             break;
         case 77:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_sticky(&current_match, result, get_string("action"));
#else
           fprintf(stderr, "cmd_sticky(%s)\n", get_string("action"));
#endif
             break;
         case 78:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_sticky(&current_match, result, get_string("action"));
#else
           fprintf(stderr, "cmd_sticky(%s)\n", get_string("action"));
#endif
             break;
         case 79:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_sticky(&current_match, result, get_string("action"));
#else
           fprintf(stderr, "cmd_sticky(%s)\n", get_string("action"));
#endif
             break;
         case 80:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_unmark(&current_match, result, get_string("mark"));
#else
           fprintf(stderr, "cmd_unmark(%s)\n", get_string("mark"));
#endif
             break;
         case 81:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_unmark(&current_match, result, get_string("mark"));
#else
           fprintf(stderr, "cmd_unmark(%s)\n", get_string("mark"));
#endif
             break;
         case 82:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_direction(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_focus_direction(%s)\n", get_string("direction"));
#endif
             break;
         case 83:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_direction(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_focus_direction(%s)\n", get_string("direction"));
#endif
             break;
         case 84:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_direction(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_focus_direction(%s)\n", get_string("direction"));
#endif
             break;
         case 85:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_direction(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_focus_direction(%s)\n", get_string("direction"));
#endif
             break;
         case 86:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_window_mode(&current_match, result, get_string("window_mode"));
#else
           fprintf(stderr, "cmd_focus_window_mode(%s)\n", get_string("window_mode"));
#endif
             break;
         case 87:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_window_mode(&current_match, result, get_string("window_mode"));
#else
           fprintf(stderr, "cmd_focus_window_mode(%s)\n", get_string("window_mode"));
#endif
             break;
         case 88:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_window_mode(&current_match, result, get_string("window_mode"));
#else
           fprintf(stderr, "cmd_focus_window_mode(%s)\n", get_string("window_mode"));
#endif
             break;
         case 89:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_level(&current_match, result, get_string("level"));
#else
           fprintf(stderr, "cmd_focus_level(%s)\n", get_string("level"));
#endif
             break;
         case 90:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus_level(&current_match, result, get_string("level"));
#else
           fprintf(stderr, "cmd_focus_level(%s)\n", get_string("level"));
#endif
             break;
         case 91:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_focus(&current_match, result);
#else
           fprintf(stderr, "cmd_focus()\n");
#endif
             break;
         case 92:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_split(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_split(%s)\n", get_string("direction"));
#endif
             break;
         case 93:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_split(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_split(%s)\n", get_string("direction"));
#endif
             break;
         case 94:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_split(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_split(%s)\n", get_string("direction"));
#endif
             break;
         case 95:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_split(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_split(%s)\n", get_string("direction"));
#endif
             break;
         case 96:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_split(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_split(%s)\n", get_string("direction"));
#endif
             break;
         case 97:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_split(&current_match, result, get_string("direction"));
#else
           fprintf(stderr, "cmd_split(%s)\n", get_string("direction"));
#endif
             break;
         case 98:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_exec(&current_match, result, get_string("nosn"), get_string("command"));
#else
           fprintf(stderr, "cmd_exec(%s, %s)\n", get_string("nosn"), get_string("command"));
#endif
             break;
         case 99:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_kill(&current_match, result, get_string("kill_mode"));
#else
           fprintf(stderr, "cmd_kill(%s)\n", get_string("kill_mode"));
#endif
             break;
         case 100:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_kill(&current_match, result, get_string("kill_mode"));
#else
           fprintf(stderr, "cmd_kill(%s)\n", get_string("kill_mode"));
#endif
             break;
         case 101:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_kill(&current_match, result, get_string("kill_mode"));
#else
           fprintf(stderr, "cmd_kill(%s)\n", get_string("kill_mode"));
#endif
             break;
         case 102:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_mark(&current_match, result, get_string("mark"), get_string("mode"), get_string("toggle"));
#else
           fprintf(stderr, "cmd_mark(%s, %s, %s)\n", get_string("mark"), get_string("mode"), get_string("toggle"));
#endif
             break;
         case 103:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_mode(&current_match, result, get_string("mode"));
#else
           fprintf(stderr, "cmd_mode(%s)\n", get_string("mode"));
#endif
             break;
         case 104:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_move_scratchpad(&current_match, result);
#else
           fprintf(stderr, "cmd_move_scratchpad()\n");
#endif
             break;
         case 105:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_nop(&current_match, result, get_string("comment"));
#else
           fprintf(stderr, "cmd_nop(%s)\n", get_string("comment"));
#endif
             break;
         case 106:
             result->next_state = INITIAL;
#ifndef TEST_PARSER
             cmd_nop(&current_match, result, NULL);
#else
           fprintf(stderr, "cmd_nop(NULL)\n");
#endif
             break;
        default:
            printf("BUG in the parser. state = %d\n", call_identifier);
            assert(false);
    }
}
