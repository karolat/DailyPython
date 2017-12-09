def note(major_scale_name, solfeage_name):
    solfege = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
    mj = build_major_scale(major_scale_name)
    return mj[solfege.index(solfeage_name)]