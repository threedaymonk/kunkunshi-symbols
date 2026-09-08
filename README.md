# Kunkunshi symbols

A set of symbols for Okinawan kunkunshi notation: kanji; pseudo-kanji (used for
notation but which don't appear in Unicode and/or in most fonts); articulations
that have a fixed symbol.

This includes symbols used for sanshin and for vocal notation.

Each symbol is stored in its own SVG file in the `src` directory, and
consists of a single `<path>` element with an ID.

The nominal size of each symbol is 18 points, and the symbol is drawn in
a canvas of 28 by 36 points, with the origin at dead centre.

## Notes

|      ID       | Kanji | Notes                    |
|---------------|-------|--------------------------|
| note_maru     | ◯     | Rest                     |
| note_ai       | 合    |                          |
| note_otsu     | 乙    |                          |
| note_rou      | 老    |                          |
| note_gerou    | 下老  |                          |
| note_koujou   | ﾛ上   |                          |
| note_kounaka  | ﾛ中   |                          |
| note_koushaku | ﾛ尺   |                          |
| note_iai      | ｲ合   |                          |
| note_iotsu    | ｲ乙   |                          |
| note_yon      | 四    |                          |
| note_jou      | 上    |                          |
| note_naka     | 中    |                          |
| note_shaku    | 尺    |                          |
| note_geshaku  | 下尺  |                          |
| note_kougo    | ﾛ五   |                          |
| note_irou     | ｲ老   |                          |
| note_iyon     | ｲ四   |                          |
| note_ijou     | ｲ上   |                          |
| note_kou      | 工    |                          |
| note_go       | 五    |                          |
| note_roku     | 六    |                          |
| note_shichi   | 七    |                          |
| note_hachi    | 八    |                          |
| note_kyuu     | 九    |                          |
| note_ishaku   | ｲ尺   |                          |
| note_ikou     | ｲ工   |                          |
| note_igo      | ｲ五   |                          |
| note_sai      | 才    | Vocal; 1 octave below 上 |
| note_bon      | 凡    | Vocal; 1 octave below 中 |
| note_shaku8   | 勺    | Vocal; 1 octave below 尺 |

## Other marks

| ID         | Appearance | Notes                    |
|------------|------------|--------------------------|
| mark_uchi  | `          | Hammer-on[^1]            |
| mark_kaki  | ⌝          | Upstroke[^1]             |
| mark_flat  | ♭          | Flat[^1]                 |
| mark_f1    | Circled 一 | 1st finger               |
| mark_f2    | Circled 二 | 2nd finger               |
| mark_f3    | Circled 三 | 3rd finger               |
| mark_f4    | Circled 四 | 4th finger               |

[^1]: These marks are placed off-centre with the intention that they can be
    overlaid directly onto the note.
