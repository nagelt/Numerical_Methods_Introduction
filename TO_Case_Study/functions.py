def add_MT_DB_geoboundaries_yaxis(ax, color='orange', style='--', alpha=0.25, lw=2, fs=10, tx=0, texts=True):
    # Hauptrogenstein
    ax.axhline(y=301-37, c=color, ls=style, alpha=alpha, lw=lw, zorder=99) #264, 69
    # Passwang
    ax.axhline(y=301-106, c=color, ls=style, alpha=alpha, lw=lw, zorder=99) # 195, 32
    # Opa sandy I
    ax.axhline(y=301-138, c=color, ls=style, alpha=alpha, lw=lw, zorder=99) #163, 36
    # Opa shaly I
    ax.axhline(y=301-174, c=color, ls=style, alpha=alpha, lw=lw, zorder=99) # 127, 12
    # Opa sandy II
    ax.axhline(y=301-186, c=color, ls=style, alpha=alpha, lw=lw, zorder=99) # 115, 4
    # Opa carbon
    ax.axhline(y=301-190, c=color, ls=style, alpha=alpha, lw=lw, zorder=99) # 111, 47
    # Opa shaly II
    ax.axhline(y=301-237, c=color, ls=style, alpha=alpha, lw=lw, zorder=99) # 64
    # Staffelegg
    #ax.axvline(x=-37, c=color, ls=style, alpha=alpha)
    if texts:
        ax.text(tx, 275, "Hauptrogenstein", size=fs, rotation='horizontal', horizontalalignment='center')
        ax.text(tx, 225, "Passwang", size=fs, rotation='horizontal', horizontalalignment='center')
        ax.text(tx, 175, "Opalinus sandy I", size=fs, rotation='horizontal', horizontalalignment='center')
        ax.text(tx, 145, "Opalinus shaly I", size=fs, rotation='horizontal', horizontalalignment='center')
        ax.text(tx, 120, "Opalinus sandy II", size=fs, rotation='horizontal', horizontalalignment='center')
        ax.text(tx, 110, "Opalinus carbonate", size=fs, rotation='horizontal', horizontalalignment='center')
        ax.text(tx, 85, "Opalinus shaly II", size=fs, rotation='horizontal', horizontalalignment='center')
        ax.text(tx, 25, "Staffelegg", size=fs, rotation='horizontal', horizontalalignment='center')
    return ax