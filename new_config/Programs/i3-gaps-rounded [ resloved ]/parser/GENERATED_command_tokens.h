static cmdp_token tokens_RENAME_WORKSPACE_LIKELY_TO_NEW_NAME[2] = {
    { "string", "new_name", __CALL, { 0 } },
    { "end", "", __CALL, { 1 } },
};
static cmdp_token tokens_RENAME_WORKSPACE_TO_NEW_NAME[1] = {
    { "string", "new_name", __CALL, { 2 } },
};
static cmdp_token tokens_RENAME_WORKSPACE_LIKELY_TO[2] = {
    { "'to ", "", RENAME_WORKSPACE_LIKELY_TO_NEW_NAME, { 0 } },
    { "word", "new_name", __CALL, { 3 } },
};
static cmdp_token tokens_MOVE_TO_ABSOLUTE_POSITION[1] = {
    { "'position", "", MOVE_TO_POSITION, { 0 } },
};
static cmdp_token tokens_MOVE_WORKSPACE_TO_OUTPUT[2] = {
    { "'output", "", MOVE_WORKSPACE_TO_OUTPUT, { 0 } },
    { "string", "output", __CALL, { 4 } },
};
static cmdp_token tokens_RESIZE_HEIGHT_GET_NUMBER[1] = {
    { "number", "height", RESIZE_HEIGHT, { 0 } },
};
static cmdp_token tokens_MOVE_WORKSPACE_NUMBER[1] = {
    { "string", "number", __CALL, { 5 } },
};
static cmdp_token tokens_RENAME_WORKSPACE_TO[1] = {
    { "'to", "", RENAME_WORKSPACE_TO_NEW_NAME, { 0 } },
};
static cmdp_token tokens_RESIZE_TILING_FINAL[2] = {
    { "'ppt", "", __CALL, { 6 } },
    { "end", "", __CALL, { 7 } },
};
static cmdp_token tokens_MOVE_TO_POSITION_X[2] = {
    { "'px", "", MOVE_TO_POSITION_X, { 0 } },
    { "number", "coord_y", MOVE_TO_POSITION_Y, { 0 } },
};
static cmdp_token tokens_MOVE_TO_POSITION_Y[2] = {
    { "'px", "", __CALL, { 8 } },
    { "end", "", __CALL, { 9 } },
};
static cmdp_token tokens_FULLSCREEN_COMPAT[2] = {
    { "'global", "mode", __CALL, { 10 } },
    { "end", "", __CALL, { 11 } },
};
static cmdp_token tokens_MOVE_DIRECTION_PX[2] = {
    { "'px", "", __CALL, { 12 } },
    { "end", "", __CALL, { 13 } },
};
static cmdp_token tokens_BAR_HIDDEN_STATE[3] = {
    { "'hide", "bar_value", BAR_W_ID, { 0 } },
    { "'show", "bar_value", BAR_W_ID, { 0 } },
    { "'toggle", "bar_value", BAR_W_ID, { 0 } },
};
static cmdp_token tokens_MOVE_TO_POSITION[5] = {
    { "'center", "", __CALL, { 14 } },
    { "'mouse", "", __CALL, { 15 } },
    { "'cursor", "", __CALL, { 16 } },
    { "'pointer", "", __CALL, { 17 } },
    { "number", "coord_x", MOVE_TO_POSITION_X, { 0 } },
};
static cmdp_token tokens_RENAME_WORKSPACE[2] = {
    { "'to", "", RENAME_WORKSPACE_LIKELY_TO, { 0 } },
    { "word", "old_name", RENAME_WORKSPACE_TO, { 0 } },
};
static cmdp_token tokens_RESIZE_DIRECTION[6] = {
    { "'up", "direction", RESIZE_PX, { 0 } },
    { "'down", "direction", RESIZE_PX, { 0 } },
    { "'left", "direction", RESIZE_PX, { 0 } },
    { "'right", "direction", RESIZE_PX, { 0 } },
    { "'width", "direction", RESIZE_PX, { 0 } },
    { "'height", "direction", RESIZE_PX, { 0 } },
};
static cmdp_token tokens_RESIZE_TILING_OR[1] = {
    { "number", "resize_ppt", RESIZE_TILING_FINAL, { 0 } },
};
static cmdp_token tokens_WORKSPACE_NUMBER[1] = {
    { "string", "workspace", __CALL, { 18 } },
};
static cmdp_token tokens_FULLSCREEN_MODE[2] = {
    { "'global", "mode", __CALL, { 19 } },
    { "end", "", __CALL, { 20 } },
};
static cmdp_token tokens_GAPS_WITH_SCOPE[4] = {
    { "'plus", "mode", GAPS_WITH_MODE, { 0 } },
    { "'minus", "mode", GAPS_WITH_MODE, { 0 } },
    { "'set", "mode", GAPS_WITH_MODE, { 0 } },
    { "'toggle", "mode", GAPS_WITH_MODE, { 0 } },
};
static cmdp_token tokens_GAPS_WITH_MODE[1] = {
    { "word", "value", __CALL, { 21 } },
};
static cmdp_token tokens_GAPS_WITH_TYPE[2] = {
    { "'current", "scope", GAPS_WITH_SCOPE, { 0 } },
    { "'all", "scope", GAPS_WITH_SCOPE, { 0 } },
};
static cmdp_token tokens_MOVE_DIRECTION[2] = {
    { "number", "pixels", MOVE_DIRECTION_PX, { 0 } },
    { "end", "", __CALL, { 22 } },
};
static cmdp_token tokens_MOVE_TO_OUTPUT[1] = {
    { "string", "output", __CALL, { 23 } },
};
static cmdp_token tokens_MOVE_WORKSPACE[9] = {
    { "'to ", "", MOVE_WORKSPACE_TO_OUTPUT, { 0 } },
    { "'next_on_output", "workspace", __CALL, { 24 } },
    { "'prev_on_output", "workspace", __CALL, { 25 } },
    { "'next", "workspace", __CALL, { 26 } },
    { "'prev", "workspace", __CALL, { 27 } },
    { "'current", "workspace", __CALL, { 28 } },
    { "'back_and_forth", "", __CALL, { 29 } },
    { "'number", "", MOVE_WORKSPACE_NUMBER, { 0 } },
    { "string", "workspace", __CALL, { 30 } },
};
static cmdp_token tokens_APPEND_LAYOUT[1] = {
    { "string", "path", __CALL, { 31 } },
};
static cmdp_token tokens_CRITERION_STR[1] = {
    { "word", "cvalue", __CALL, { 32 } },
};
static cmdp_token tokens_LAYOUT_TOGGLE[2] = {
    { "end", "", __CALL, { 33 } },
    { "string", "toggle_mode", __CALL, { 34 } },
};
static cmdp_token tokens_RESIZE_HEIGHT[3] = {
    { "'px", "mode_height", RESIZE_HEIGHT, { 0 } },
    { "'ppt", "mode_height", RESIZE_HEIGHT, { 0 } },
    { "end", "", __CALL, { 35 } },
};
static cmdp_token tokens_RESIZE_TILING[3] = {
    { "'px", "", RESIZE_TILING, { 0 } },
    { "'or", "", RESIZE_TILING_OR, { 0 } },
    { "end", "", __CALL, { 36 } },
};
static cmdp_token tokens_SWAP_ARGUMENT[1] = {
    { "string", "arg", __CALL, { 37 } },
};
static cmdp_token tokens_BORDER_WIDTH[2] = {
    { "end", "", __CALL, { 38 } },
    { "number", "border_width", __CALL, { 39 } },
};
static cmdp_token tokens_FOCUS_OUTPUT[1] = {
    { "string", "output", __CALL, { 40 } },
};
static cmdp_token tokens_MOVE_TO_MARK[1] = {
    { "string", "mark", __CALL, { 41 } },
};
static cmdp_token tokens_RESIZE_WIDTH[5] = {
    { "'px", "mode_width", RESIZE_WIDTH, { 0 } },
    { "'ppt", "mode_width", RESIZE_WIDTH, { 0 } },
    { "end", "", __CALL, { 42 } },
    { "'height", "", RESIZE_HEIGHT_GET_NUMBER, { 0 } },
    { "number", "height", RESIZE_HEIGHT, { 0 } },
};
static cmdp_token tokens_TITLE_FORMAT[1] = {
    { "string", "format", __CALL, { 43 } },
};
static cmdp_token tokens_FULLSCREEN[4] = {
    { "'disable", "action", __CALL, { 44 } },
    { "'enable", "action", FULLSCREEN_MODE, { 0 } },
    { "'toggle", "action", FULLSCREEN_MODE, { 0 } },
    { "'", "action", FULLSCREEN_COMPAT, { 0 } },
};
static cmdp_token tokens_RESIZE_SET[3] = {
    { "'height", "", RESIZE_HEIGHT_GET_NUMBER, { 0 } },
    { "'width", "", RESIZE_SET, { 0 } },
    { "number", "width", RESIZE_WIDTH, { 0 } },
};
static cmdp_token tokens_SCRATCHPAD[1] = {
    { "'show", "", __CALL, { 45 } },
};
static cmdp_token tokens_CRITERION[1] = {
    { "'=", "", CRITERION_STR, { 0 } },
};
static cmdp_token tokens_RESIZE_PX[2] = {
    { "number", "resize_px", RESIZE_TILING, { 0 } },
    { "end", "", __CALL, { 46 } },
};
static cmdp_token tokens_WORKSPACE[8] = {
    { "'--no-auto-back-and-forth", "no_auto_back_and_forth", WORKSPACE, { 0 } },
    { "'next_on_output", "direction", __CALL, { 47 } },
    { "'prev_on_output", "direction", __CALL, { 48 } },
    { "'next", "direction", __CALL, { 49 } },
    { "'prev", "direction", __CALL, { 50 } },
    { "'back_and_forth", "", __CALL, { 51 } },
    { "'number", "", WORKSPACE_NUMBER, { 0 } },
    { "string", "workspace", __CALL, { 52 } },
};
static cmdp_token tokens_BAR_MODE[4] = {
    { "'dock", "bar_value", BAR_W_ID, { 0 } },
    { "'hide", "bar_value", BAR_W_ID, { 0 } },
    { "'invisible", "bar_value", BAR_W_ID, { 0 } },
    { "'toggle", "bar_value", BAR_W_ID, { 0 } },
};
static cmdp_token tokens_BAR_W_ID[2] = {
    { "word", "bar_id", BAR_W_ID, { 0 } },
    { "end", "", __CALL, { 53 } },
};
static cmdp_token tokens_CRITERIA[13] = {
    { "'class", "ctype", CRITERION, { 0 } },
    { "'instance", "ctype", CRITERION, { 0 } },
    { "'window_role", "ctype", CRITERION, { 0 } },
    { "'con_id", "ctype", CRITERION, { 0 } },
    { "'id", "ctype", CRITERION, { 0 } },
    { "'window_type", "ctype", CRITERION, { 0 } },
    { "'con_mark", "ctype", CRITERION, { 0 } },
    { "'title", "ctype", CRITERION, { 0 } },
    { "'urgent", "ctype", CRITERION, { 0 } },
    { "'workspace", "ctype", CRITERION, { 0 } },
    { "'tiling", "ctype", __CALL, { 54 } },
    { "'floating", "ctype", __CALL, { 55 } },
    { "']", "", __CALL, { 56 } },
};
static cmdp_token tokens_DEBUGLOG[3] = {
    { "'toggle", "argument", __CALL, { 57 } },
    { "'on", "argument", __CALL, { 58 } },
    { "'off", "argument", __CALL, { 59 } },
};
static cmdp_token tokens_FLOATING[3] = {
    { "'enable", "floating", __CALL, { 60 } },
    { "'disable", "floating", __CALL, { 61 } },
    { "'toggle", "floating", __CALL, { 62 } },
};
static cmdp_token tokens_INITIAL[31] = {
    { "end", "", INITIAL, { 0 } },
    { "'[", "", __CALL, { 63 } },
    { "'move", "", MOVE, { 0 } },
    { "'exec", "", EXEC, { 0 } },
    { "'exit", "", __CALL, { 64 } },
    { "'restart", "", __CALL, { 65 } },
    { "'reload", "", __CALL, { 66 } },
    { "'shmlog", "", SHMLOG, { 0 } },
    { "'debuglog", "", DEBUGLOG, { 0 } },
    { "'border", "", BORDER, { 0 } },
    { "'layout", "", LAYOUT, { 0 } },
    { "'append_layout", "", APPEND_LAYOUT, { 0 } },
    { "'workspace", "", WORKSPACE, { 0 } },
    { "'focus", "", FOCUS, { 0 } },
    { "'kill", "", KILL, { 0 } },
    { "'open", "", __CALL, { 67 } },
    { "'fullscreen", "", FULLSCREEN, { 0 } },
    { "'sticky", "", STICKY, { 0 } },
    { "'split", "", SPLIT, { 0 } },
    { "'floating", "", FLOATING, { 0 } },
    { "'mark", "", MARK, { 0 } },
    { "'unmark", "", UNMARK, { 0 } },
    { "'resize", "", RESIZE, { 0 } },
    { "'rename", "", RENAME, { 0 } },
    { "'nop", "", NOP, { 0 } },
    { "'scratchpad", "", SCRATCHPAD, { 0 } },
    { "'swap", "", SWAP, { 0 } },
    { "'title_format", "", TITLE_FORMAT, { 0 } },
    { "'mode", "", MODE, { 0 } },
    { "'bar", "", BAR, { 0 } },
    { "'gaps", "", GAPS, { 0 } },
};
static cmdp_token tokens_BORDER[5] = {
    { "'normal", "border_style", BORDER_WIDTH, { 0 } },
    { "'pixel", "border_style", BORDER_WIDTH, { 0 } },
    { "'toggle", "border_style", BORDER_WIDTH, { 0 } },
    { "'none", "border_style", __CALL, { 68 } },
    { "'1pixel", "", __CALL, { 69 } },
};
static cmdp_token tokens_LAYOUT[7] = {
    { "'default", "layout_mode", __CALL, { 70 } },
    { "'stacked", "layout_mode", __CALL, { 71 } },
    { "'stacking", "layout_mode", __CALL, { 72 } },
    { "'tabbed", "layout_mode", __CALL, { 73 } },
    { "'splitv", "layout_mode", __CALL, { 74 } },
    { "'splith", "layout_mode", __CALL, { 75 } },
    { "'toggle", "", LAYOUT_TOGGLE, { 0 } },
};
static cmdp_token tokens_RENAME[1] = {
    { "'workspace", "", RENAME_WORKSPACE, { 0 } },
};
static cmdp_token tokens_RESIZE[3] = {
    { "'grow", "way", RESIZE_DIRECTION, { 0 } },
    { "'shrink", "way", RESIZE_DIRECTION, { 0 } },
    { "'set", "set", RESIZE_SET, { 0 } },
};
static cmdp_token tokens_SHMLOG[1] = {
    { "string", "argument", __CALL, { 76 } },
};
static cmdp_token tokens_STICKY[3] = {
    { "'enable", "action", __CALL, { 77 } },
    { "'disable", "action", __CALL, { 78 } },
    { "'toggle", "action", __CALL, { 79 } },
};
static cmdp_token tokens_UNMARK[2] = {
    { "end", "", __CALL, { 80 } },
    { "string", "mark", __CALL, { 81 } },
};
static cmdp_token tokens_FOCUS[11] = {
    { "'left", "direction", __CALL, { 82 } },
    { "'right", "direction", __CALL, { 83 } },
    { "'up", "direction", __CALL, { 84 } },
    { "'down", "direction", __CALL, { 85 } },
    { "'output", "", FOCUS_OUTPUT, { 0 } },
    { "'tiling", "window_mode", __CALL, { 86 } },
    { "'floating", "window_mode", __CALL, { 87 } },
    { "'mode_toggle", "window_mode", __CALL, { 88 } },
    { "'parent", "level", __CALL, { 89 } },
    { "'child", "level", __CALL, { 90 } },
    { "end", "", __CALL, { 91 } },
};
static cmdp_token tokens_SPLIT[6] = {
    { "'horizontal", "direction", __CALL, { 92 } },
    { "'vertical", "direction", __CALL, { 93 } },
    { "'toggle", "direction", __CALL, { 94 } },
    { "'v", "direction", __CALL, { 95 } },
    { "'h", "direction", __CALL, { 96 } },
    { "'t", "direction", __CALL, { 97 } },
};
static cmdp_token tokens_EXEC[2] = {
    { "'--no-startup-id", "nosn", EXEC, { 0 } },
    { "string", "command", __CALL, { 98 } },
};
static cmdp_token tokens_GAPS[8] = {
    { "'inner", "type", GAPS_WITH_TYPE, { 0 } },
    { "'outer", "type", GAPS_WITH_TYPE, { 0 } },
    { "'horizontal", "type", GAPS_WITH_TYPE, { 0 } },
    { "'vertical", "type", GAPS_WITH_TYPE, { 0 } },
    { "'top", "type", GAPS_WITH_TYPE, { 0 } },
    { "'right", "type", GAPS_WITH_TYPE, { 0 } },
    { "'bottom", "type", GAPS_WITH_TYPE, { 0 } },
    { "'left", "type", GAPS_WITH_TYPE, { 0 } },
};
static cmdp_token tokens_KILL[3] = {
    { "'window", "kill_mode", __CALL, { 99 } },
    { "'client", "kill_mode", __CALL, { 100 } },
    { "end", "", __CALL, { 101 } },
};
static cmdp_token tokens_MARK[4] = {
    { "'--add", "mode", MARK, { 0 } },
    { "'--replace", "mode", MARK, { 0 } },
    { "'--toggle", "toggle", MARK, { 0 } },
    { "string", "mark", __CALL, { 102 } },
};
static cmdp_token tokens_MODE[1] = {
    { "string", "mode", __CALL, { 103 } },
};
static cmdp_token tokens_MOVE[14] = {
    { "'window", "", MOVE, { 0 } },
    { "'container", "", MOVE, { 0 } },
    { "'to", "", MOVE, { 0 } },
    { "'--no-auto-back-and-forth", "no_auto_back_and_forth", MOVE, { 0 } },
    { "'workspace", "", MOVE_WORKSPACE, { 0 } },
    { "'output", "", MOVE_TO_OUTPUT, { 0 } },
    { "'mark", "", MOVE_TO_MARK, { 0 } },
    { "'scratchpad", "", __CALL, { 104 } },
    { "'left", "direction", MOVE_DIRECTION, { 0 } },
    { "'right", "direction", MOVE_DIRECTION, { 0 } },
    { "'up", "direction", MOVE_DIRECTION, { 0 } },
    { "'down", "direction", MOVE_DIRECTION, { 0 } },
    { "'position", "method", MOVE_TO_POSITION, { 0 } },
    { "'absolute", "method", MOVE_TO_ABSOLUTE_POSITION, { 0 } },
};
static cmdp_token tokens_SWAP[5] = {
    { "'container", "", SWAP, { 0 } },
    { "'with", "", SWAP, { 0 } },
    { "'id", "mode", SWAP_ARGUMENT, { 0 } },
    { "'con_id", "mode", SWAP_ARGUMENT, { 0 } },
    { "'mark", "mode", SWAP_ARGUMENT, { 0 } },
};
static cmdp_token tokens_BAR[2] = {
    { "'hidden_state", "bar_type", BAR_HIDDEN_STATE, { 0 } },
    { "'mode", "bar_type", BAR_MODE, { 0 } },
};
static cmdp_token tokens_NOP[2] = {
    { "string", "comment", __CALL, { 105 } },
    { "end", "", __CALL, { 106 } },
};
static cmdp_token_ptr tokens[67] = {
    { tokens_RENAME_WORKSPACE_LIKELY_TO_NEW_NAME, 2 },
    { tokens_RENAME_WORKSPACE_TO_NEW_NAME, 1 },
    { tokens_RENAME_WORKSPACE_LIKELY_TO, 2 },
    { tokens_MOVE_TO_ABSOLUTE_POSITION, 1 },
    { tokens_MOVE_WORKSPACE_TO_OUTPUT, 2 },
    { tokens_RESIZE_HEIGHT_GET_NUMBER, 1 },
    { tokens_MOVE_WORKSPACE_NUMBER, 1 },
    { tokens_RENAME_WORKSPACE_TO, 1 },
    { tokens_RESIZE_TILING_FINAL, 2 },
    { tokens_MOVE_TO_POSITION_X, 2 },
    { tokens_MOVE_TO_POSITION_Y, 2 },
    { tokens_FULLSCREEN_COMPAT, 2 },
    { tokens_MOVE_DIRECTION_PX, 2 },
    { tokens_BAR_HIDDEN_STATE, 3 },
    { tokens_MOVE_TO_POSITION, 5 },
    { tokens_RENAME_WORKSPACE, 2 },
    { tokens_RESIZE_DIRECTION, 6 },
    { tokens_RESIZE_TILING_OR, 1 },
    { tokens_WORKSPACE_NUMBER, 1 },
    { tokens_FULLSCREEN_MODE, 2 },
    { tokens_GAPS_WITH_SCOPE, 4 },
    { tokens_GAPS_WITH_MODE, 1 },
    { tokens_GAPS_WITH_TYPE, 2 },
    { tokens_MOVE_DIRECTION, 2 },
    { tokens_MOVE_TO_OUTPUT, 1 },
    { tokens_MOVE_WORKSPACE, 9 },
    { tokens_APPEND_LAYOUT, 1 },
    { tokens_CRITERION_STR, 1 },
    { tokens_LAYOUT_TOGGLE, 2 },
    { tokens_RESIZE_HEIGHT, 3 },
    { tokens_RESIZE_TILING, 3 },
    { tokens_SWAP_ARGUMENT, 1 },
    { tokens_BORDER_WIDTH, 2 },
    { tokens_FOCUS_OUTPUT, 1 },
    { tokens_MOVE_TO_MARK, 1 },
    { tokens_RESIZE_WIDTH, 5 },
    { tokens_TITLE_FORMAT, 1 },
    { tokens_FULLSCREEN, 4 },
    { tokens_RESIZE_SET, 3 },
    { tokens_SCRATCHPAD, 1 },
    { tokens_CRITERION, 1 },
    { tokens_RESIZE_PX, 2 },
    { tokens_WORKSPACE, 8 },
    { tokens_BAR_MODE, 4 },
    { tokens_BAR_W_ID, 2 },
    { tokens_CRITERIA, 13 },
    { tokens_DEBUGLOG, 3 },
    { tokens_FLOATING, 3 },
    { tokens_INITIAL, 31 },
    { tokens_BORDER, 5 },
    { tokens_LAYOUT, 7 },
    { tokens_RENAME, 1 },
    { tokens_RESIZE, 3 },
    { tokens_SHMLOG, 1 },
    { tokens_STICKY, 3 },
    { tokens_UNMARK, 2 },
    { tokens_FOCUS, 11 },
    { tokens_SPLIT, 6 },
    { tokens_EXEC, 2 },
    { tokens_GAPS, 8 },
    { tokens_KILL, 3 },
    { tokens_MARK, 4 },
    { tokens_MODE, 1 },
    { tokens_MOVE, 14 },
    { tokens_SWAP, 5 },
    { tokens_BAR, 2 },
    { tokens_NOP, 2 },
};
