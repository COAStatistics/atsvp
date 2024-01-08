! function(e, t, i, a) {
    function o(t, i) {
        this.obj = e(t), this.o = e.extend({}, e.fn[s].defaults, i), this.objId = this.obj.attr("id"), this.pwCtrls = ".jarviswidget-ctrls", this.widget = this.obj.find(this.o.widgets), this.toggleClass = this.o.toggleClass.split("|"), this.editClass = this.o.editClass.split("|"), this.fullscreenClass = this.o.fullscreenClass.split("|"), this.customClass = this.o.customClass.split("|"), this.storage = {
            enabled: this.o.localStorage
        }, this.initialized = !1, this.init()
    }
    var s = "jarvisWidgets",
        l = ("ontouchstart" in t || t.DocumentTouch && i instanceof DocumentTouch ? "clickEvent" : "click") + "." + s;
    o.prototype = {
        _runLoaderWidget: function(e) {
            var t = this;
            !0 === t.o.indicator && e.parents(t.o.widgets).find(".jarviswidget-loader:first").stop(!0, !0).fadeIn(100).delay(t.o.indicatorTime).fadeOut(100)
        },
        _getPastTimestamp: function(e) {
            var t = this,
                i = new Date(e),
                a = i.getMonth() + 1,
                o = i.getDate(),
                s = i.getFullYear(),
                l = i.getHours(),
                d = i.getMinutes(),
                n = i.getUTCSeconds();
            return a < 10 && (a = "0" + a), o < 10 && (o = "0" + o), l < 10 && (l = "0" + l), d < 10 && (d = "0" + d), n < 10 && (n = "0" + n), t.o.timestampFormat.replace(/%d%/g, o).replace(/%m%/g, a).replace(/%y%/g, s).replace(/%h%/g, l).replace(/%i%/g, d).replace(/%s%/g, n)
        },
        _loadAjaxFile: function(t, i, a) {
            var o = this;
            t.find(".widget-body").load(i, function(i, a, s) {
                var l = e(this);
                if ("error" == a && l.html('<h4 class="alert alert-danger">' + o.o.labelError + "<b> " + s.status + " " + s.statusText + "</b></h4>"), "success" == a) {
                    var d = t.find(o.o.timestampPlaceholder);
                    d.length && d.html(o._getPastTimestamp(new Date)), "function" == typeof o.o.afterLoad && o.o.afterLoad.call(this, t)
                }
                o = null
            }), this._runLoaderWidget(a)
        },
        _loadKeys: function() {
            var e = this;
            if (!0 === e.o.ajaxnav) {
                t = location.hash.replace(/^#/, "");
                e.storage.keySettings = "Plugin_settings_" + t + "_" + e.objId, e.storage.keyPosition = "Plugin_position_" + t + "_" + e.objId
            } else if (!1 === e.initialized) {
                var t = e.o.pageKey || location.pathname;
                e.storage.keySettings = "jarvisWidgets_settings_" + t + "_" + e.objId, e.storage.keyPosition = "jarvisWidgets_position_" + t + "_" + e.objId
            }
        },
        _saveSettingsWidget: function() {
            var t = this,
                i = t.storage;
            t._loadKeys();
            var a = t.obj.find(t.o.widgets).map(function() {
                    var t = {};
                    return t.id = e(this).attr("id"), t.style = e(this).attr("data-widget-attstyle"), t.title = e(this).children("header").children("h2").text(), t.hidden = "none" == e(this).css("display") ? 1 : 0, t.collapsed = e(this).hasClass("jarviswidget-collapsed") ? 1 : 0, t
                }).get(),
                o = JSON.stringify({
                    widget: a
                });
            i.enabled && i.getKeySettings != o && (localStorage.setItem(i.keySettings, o), i.getKeySettings = o), "function" == typeof t.o.onSave && t.o.onSave.call(this, null, o, i.keySettings)
        },
        _savePositionWidget: function() {
            var t = this,
                i = t.storage;
            t._loadKeys();
            var a = t.obj.find(t.o.grid + ".sortable-grid").map(function() {
                    return {
                        section: e(this).children(t.o.widgets).map(function() {
                            return {
                                id: e(this).attr("id")
                            }
                        }).get()
                    }
                }).get(),
                o = JSON.stringify({
                    grid: a
                });
            i.enabled && i.getKeyPosition != o && (localStorage.setItem(i.keyPosition, o), i.getKeyPosition = o), "function" == typeof t.o.onSave && t.o.onSave.call(this, o, i.keyPosition)
        },
        init: function() {
            var t = this;
            if (!t.initialized) {
                if (t._initStorage(t.storage), e("#" + t.objId).length || alert("It looks like your using a class instead of an ID, dont do that!"), !0 === t.o.rtl && e("body").addClass("rtl"), e(t.o.grid).each(function() {
                        e(this).find(t.o.widgets).length && e(this).addClass("sortable-grid")
                    }), t.storage.enabled && t.storage.getKeyPosition) {
                    var i = JSON.parse(t.storage.getKeyPosition);
                    for (var a in i.grid) {
                        var o = t.obj.find(t.o.grid + ".sortable-grid").eq(a);
                        for (var d in i.grid[a].section) o.append(e("#" + i.grid[a].section[d].id))
                    }
                }
                if (t.storage.enabled && t.storage.getKeySettings) {
                    var n = JSON.parse(t.storage.getKeySettings);
                    for (var a in n.widget) {
                        var r = e("#" + n.widget[a].id);
                        n.widget[a].style && r.removeClassPrefix("jarviswidget-color-").addClass(n.widget[a].style).attr("data-widget-attstyle", "" + n.widget[a].style), 1 == n.widget[a].hidden ? r.hide(1) : r.show(1).removeAttr("data-widget-hidden"), 1 == n.widget[a].collapsed && r.addClass("jarviswidget-collapsed").children("div").hide(1), r.children("header").children("h2").text() != n.widget[a].title && r.children("header").children("h2").text(n.widget[a].title)
                    }
                }
                if (t.widget.each(function() {
                        var i, a, o, s, l, d, n, r = e(this),
                            g = e(this).children("header");
                        if (!g.parent().attr("role")) {
                            !0 === r.data("widget-hidden") && r.hide(), !0 === r.data("widget-collapsed") && r.addClass("jarviswidget-collapsed").children("div").hide(), i = !0 === t.o.customButton && void 0 === r.data("widget-custombutton") && 0 !== t.customClass[0].length ? '<a href="javascript:void(0);" class="button-icon jarviswidget-custom-btn"><i class="' + t.customClass[0] + '"></i></a>' : "", a = !0 === t.o.deleteButton && void 0 === r.data("widget-deletebutton") ? '<a href="javascript:void(0);" class="button-icon jarviswidget-delete-btn" rel="tooltip" title="Delete" data-placement="bottom"><i class="' + t.o.deleteClass + '"></i></a>' : "", o = !0 === t.o.editButton && void 0 === r.data("widget-editbutton") ? '<a href="javascript:void(0);" class="button-icon jarviswidget-edit-btn" rel="tooltip" title="Edit" data-placement="bottom"><i class="' + t.editClass[0] + '"></i></a>' : "", s = !0 === t.o.fullscreenButton && void 0 === r.data("widget-fullscreenbutton") ? '<a href="javascript:void(0);" class="button-icon jarviswidget-fullscreen-btn" rel="tooltip" title="Fullscreen" data-placement="bottom"><i class="' + t.fullscreenClass[0] + '"></i></a>' : "", !0 === t.o.colorButton && void 0 === r.data("widget-colorbutton") ? (l = '<a data-toggle="dropdown" class="dropdown-toggle color-box selector" href="javascript:void(0);"></a><ul class="dropdown-menu arrow-box-up-right color-select pull-right"><li><span class="bg-color-green" data-widget-setstyle="jarviswidget-color-green" rel="tooltip" data-placement="left" data-original-title="Green Grass"></span></li><li><span class="bg-color-greenDark" data-widget-setstyle="jarviswidget-color-greenDark" rel="tooltip" data-placement="top" data-original-title="Dark Green"></span></li><li><span class="bg-color-greenLight" data-widget-setstyle="jarviswidget-color-greenLight" rel="tooltip" data-placement="top" data-original-title="Light Green"></span></li><li><span class="bg-color-purple" data-widget-setstyle="jarviswidget-color-purple" rel="tooltip" data-placement="top" data-original-title="Purple"></span></li><li><span class="bg-color-magenta" data-widget-setstyle="jarviswidget-color-magenta" rel="tooltip" data-placement="top" data-original-title="Magenta"></span></li><li><span class="bg-color-pink" data-widget-setstyle="jarviswidget-color-pink" rel="tooltip" data-placement="right" data-original-title="Pink"></span></li><li><span class="bg-color-pinkDark" data-widget-setstyle="jarviswidget-color-pinkDark" rel="tooltip" data-placement="left" data-original-title="Fade Pink"></span></li><li><span class="bg-color-blueLight" data-widget-setstyle="jarviswidget-color-redLight" rel="tooltip" data-placement="top" data-original-title="Light Blue"></span></li><li><span class="bg-color-teal" data-widget-setstyle="jarviswidget-color-teal" rel="tooltip" data-placement="top" data-original-title="Teal"></span></li><li><span class="bg-color-blue" data-widget-setstyle="jarviswidget-color-blue" rel="tooltip" data-placement="top" data-original-title="Ocean Blue"></span></li><li><span class="bg-color-blueDark" data-widget-setstyle="jarviswidget-color-blueDark" rel="tooltip" data-placement="top" data-original-title="Night Sky"></span></li><li><span class="bg-color-darken" data-widget-setstyle="jarviswidget-color-darken" rel="tooltip" data-placement="right" data-original-title="Night"></span></li><li><span class="bg-color-yellow" data-widget-setstyle="jarviswidget-color-yellow" rel="tooltip" data-placement="left" data-original-title="Day Light"></span></li><li><span class="bg-color-orange" data-widget-setstyle="jarviswidget-color-orange" rel="tooltip" data-placement="bottom" data-original-title="Orange"></span></li><li><span class="bg-color-orangeDark" data-widget-setstyle="jarviswidget-color-orangeDark" rel="tooltip" data-placement="bottom" data-original-title="Dark Orange"></span></li><li><span class="bg-color-red" data-widget-setstyle="jarviswidget-color-red" rel="tooltip" data-placement="bottom" data-original-title="Red Rose"></span></li><li><span class="bg-color-redLight" data-widget-setstyle="jarviswidget-color-redLight" rel="tooltip" data-placement="bottom" data-original-title="Light Red"></span></li><li><span class="bg-color-white" data-widget-setstyle="jarviswidget-color-white" rel="tooltip" data-placement="right" data-original-title="Purity"></span></li><li><a href="javascript:void(0);" class="jarviswidget-remove-colors" data-widget-setstyle="" rel="tooltip" data-placement="bottom" data-original-title="Reset widget color to default">Remove</a></li></ul>', g.prepend('<div class="widget-toolbar">' + l + "</div>")) : l = "", d = !0 === t.o.toggleButton && void 0 === r.data("widget-togglebutton") ? '<a href="javascript:void(0);" class="button-icon jarviswidget-toggle-btn" rel="tooltip" title="Collapse" data-placement="bottom"><i class="' + (!0 === r.data("widget-collapsed") || r.hasClass("jarviswidget-collapsed") ? t.toggleClass[1] : t.toggleClass[0]) + '"></i></a>' : "", n = !0 === t.o.refreshButton && !1 !== r.data("widget-refreshbutton") && r.data("widget-load") ? '<a href="javascript:void(0);" class="button-icon jarviswidget-refresh-btn" data-loading-text="&nbsp;&nbsp;Loading...&nbsp;" rel="tooltip" title="Refresh" data-placement="bottom"><i class="' + t.o.refreshButtonClass + '"></i></a>' : "";
                            var c = t.o.buttonOrder.replace(/%refresh%/g, n).replace(/%delete%/g, a).replace(/%custom%/g, i).replace(/%fullscreen%/g, s).replace(/%edit%/g, o).replace(/%toggle%/g, d);
                            "" === n && "" === a && "" === i && "" === s && "" === o && "" === d || g.prepend('<div class="jarviswidget-ctrls">' + c + "</div>"), !0 === t.o.sortable && void 0 === r.data("widget-sortable") && r.addClass("jarviswidget-sortable"), r.find(t.o.editPlaceholder).length && r.find(t.o.editPlaceholder).find("input").val(e.trim(g.children("h2").text())), g.append('<span class="jarviswidget-loader"><i class="fa fa-refresh fa-spin"></i></span>'), r.attr("role", "widget").children("div").attr("role", "content").prev("header").attr("role", "heading").children("div").attr("role", "menu")
                        }
                    }), !0 === t.o.buttonsHidden && e(t.o.pwCtrls).hide(), e(".jarviswidget header [rel=tooltip]").tooltip(), t.obj.find("[data-widget-load]").each(function() {
                        var i = e(this),
                            a = i.children(),
                            o = i.data("widget-load"),
                            s = 1e3 * i.data("widget-refresh");
                        i.children();
                        i.find(".jarviswidget-ajax-placeholder").length || (i.children("widget-body").append('<div class="jarviswidget-ajax-placeholder">' + t.o.loadingLabel + "</div>"), i.data("widget-refresh") > 0 ? (t._loadAjaxFile(i, o, a), e.intervalArr.push(setInterval(function() {
                            t._loadAjaxFile(i, o, a)
                        }, s))) : t._loadAjaxFile(i, o, a))
                    }), !0 === t.o.sortable && jQuery.ui) {
                    var g = t.obj.find(t.o.grid + ".sortable-grid").not("[data-widget-excludegrid]");
                    g.sortable({
                        items: g.find(t.o.widgets + ".jarviswidget-sortable"),
                        connectWith: g,
                        placeholder: t.o.placeholderClass,
                        cursor: "move",
                        revert: !0,
                        opacity: t.o.opacity,
                        delay: 200,
                        cancel: ".button-icon, #jarviswidget-fullscreen-mode > div",
                        zIndex: 1e4,
                        handle: t.o.dragHandle,
                        forcePlaceholderSize: !0,
                        forceHelperSize: !0,
                        update: function(e, i) {
                            t._runLoaderWidget(i.item.children()), t._savePositionWidget(), "function" == typeof t.o.onChange && t.o.onChange.call(this, i.item)
                        }
                    })
                }!0 === t.o.buttonsHidden && t.widget.children("header").on("mouseenter." + s, function() {
                    e(this).children(t.o.pwCtrls).stop(!0, !0).fadeTo(100, 1)
                }).on("mouseleave." + s, function() {
                    e(this).children(t.o.pwCtrls).stop(!0, !0).fadeTo(100, 0)
                }), t._clickEvents(), t.storage.enabled && (e(t.o.deleteSettingsKey).on(l, this, function(e) {
                    confirm(t.o.settingsKeyLabel) && localStorage.removeItem(keySettings), e.preventDefault()
                }), e(t.o.deletePositionKey).on(l, this, function(e) {
                    confirm(t.o.positionKeyLabel) && localStorage.removeItem(keyPosition), e.preventDefault()
                })), initialized = !0
            }
        },
        _initStorage: function(e) {
            e.enabled = e.enabled && !! function() {
                var e, t = +new Date;
                try {
                    return localStorage.setItem(t, t), e = localStorage.getItem(t) == t, localStorage.removeItem(t), e
                } catch (e) {}
            }(), this._loadKeys(), e.enabled && (e.getKeySettings = localStorage.getItem(e.keySettings), e.getKeyPosition = localStorage.getItem(e.keyPosition))
        },
        _clickEvents: function() {
            function i() {
                if (e("#jarviswidget-fullscreen-mode").length) {
                    var i = e(t).height(),
                        o = e("#jarviswidget-fullscreen-mode").children(a.o.widgets).children("header").height();
                    e("#jarviswidget-fullscreen-mode").children(a.o.widgets).children("div").height(i - o - 15)
                }
            }
            var a = this,
                o = a.widget.children("header");
            o.on(l, ".jarviswidget-toggle-btn", function(t) {
                var i = e(this),
                    o = i.parents(a.o.widgets);
                a._runLoaderWidget(i), o.hasClass("jarviswidget-collapsed") ? i.children().removeClass(a.toggleClass[1]).addClass(a.toggleClass[0]).parents(a.o.widgets).removeClass("jarviswidget-collapsed").children("[role=content]").slideDown(a.o.toggleSpeed, function() {
                    a._saveSettingsWidget()
                }) : i.children().removeClass(a.toggleClass[0]).addClass(a.toggleClass[1]).parents(a.o.widgets).addClass("jarviswidget-collapsed").children("[role=content]").slideUp(a.o.toggleSpeed, function() {
                    a._saveSettingsWidget()
                }), "function" == typeof a.o.onToggle && a.o.onToggle.call(this, o), t.preventDefault()
            }), o.on(l, ".jarviswidget-fullscreen-btn", function(t) {
                var o = e(this).parents(a.o.widgets),
                    s = o.children("div");
                a._runLoaderWidget(e(this)), e("#jarviswidget-fullscreen-mode").length ? (e(".nooverflow").removeClass("nooverflow"), o.unwrap("#jarviswidget-fullscreen-mode").children("div").removeAttr("style").end().find(".jarviswidget-fullscreen-btn:first").children().removeClass(a.fullscreenClass[1]).addClass(a.fullscreenClass[0]).parents(a.pwCtrls).children("a").show(), s.hasClass("jarviswidget-visible") && s.hide().removeClass("jarviswidget-visible")) : (e("body").addClass("nooverflow"), o.wrap('<div id="jarviswidget-fullscreen-mode"/>').parent().find(".jarviswidget-fullscreen-btn:first").children().removeClass(a.fullscreenClass[0]).addClass(a.fullscreenClass[1]).parents(a.pwCtrls).children("a:not(.jarviswidget-fullscreen-btn)").hide(), s.is(":hidden") && s.show().addClass("jarviswidget-visible")), i(), "function" == typeof a.o.onFullscreen && a.o.onFullscreen.call(this, o), t.preventDefault()
            }), e(t).on("resize." + s, function() {
                i()
            }), o.on(l, ".jarviswidget-edit-btn", function(t) {
                var i = e(this).parents(a.o.widgets);
                a._runLoaderWidget(e(this)), i.find(a.o.editPlaceholder).is(":visible") ? e(this).children().removeClass(a.editClass[1]).addClass(a.editClass[0]).parents(a.o.widgets).find(a.o.editPlaceholder).slideUp(a.o.editSpeed, function() {
                    a._saveSettingsWidget()
                }) : e(this).children().removeClass(a.editClass[0]).addClass(a.editClass[1]).parents(a.o.widgets).find(a.o.editPlaceholder).slideDown(a.o.editSpeed), "function" == typeof a.o.onEdit && a.o.onEdit.call(this, i), t.preventDefault()
            }), e(a.o.editPlaceholder).find("input").keyup(function() {
                e(this).parents(a.o.widgets).children("header").children("h2").text(e(this).val())
            }), o.on(l, "[data-widget-setstyle]", function(t) {
                var i = e(this).data("widget-setstyle"),
                    o = "";
                e(this).parents(a.o.editPlaceholder).find("[data-widget-setstyle]").each(function() {
                    o += e(this).data("widget-setstyle") + " "
                }), e(this).parents(a.o.widgets).attr("data-widget-attstyle", "" + i).removeClassPrefix("jarviswidget-color-").addClass(i), a._runLoaderWidget(e(this)), a._saveSettingsWidget(), t.preventDefault()
            }), o.on(l, ".jarviswidget-custom-btn", function(t) {
                var i = e(this).parents(a.o.widgets);
                a._runLoaderWidget(e(this)), e(this).children("." + a.customClass[0]).length ? (e(this).children().removeClass(a.customClass[0]).addClass(a.customClass[1]), "function" == typeof a.o.customStart && a.o.customStart.call(this, i)) : (e(this).children().removeClass(a.customClass[1]).addClass(a.customClass[0]), "function" == typeof a.o.customEnd && a.o.customEnd.call(this, i)), a._saveSettingsWidget(), t.preventDefault()
            }), o.on(l, ".jarviswidget-delete-btn", function(t) {
                var i = e(this).parents(a.o.widgets),
                    o = i.attr("id"),
                    s = i.children("header").children("h2").text();
                e.SmartMessageBox ? e.SmartMessageBox({
                    title: "<i class='fa fa-times' style='color:#ed1c24'></i> " + a.o.labelDelete + ' "' + s + '"',
                    content: a.o.deleteMsg,
                    buttons: "[No][Yes]"
                }, function(t) {
                    "Yes" == t && (a._runLoaderWidget(e(this)), e("#" + o).fadeOut(a.o.deleteSpeed, function() {
                        e(this).remove(), "function" == typeof a.o.onDelete && a.o.onDelete.call(this, i)
                    }))
                }) : e("#" + o).fadeOut(a.o.deleteSpeed, function() {
                    e(this).remove(), "function" == typeof a.o.onDelete && a.o.onDelete.call(this, i)
                }), t.preventDefault()
            }), o.on(l, ".jarviswidget-refresh-btn", function(t) {
                var i = e(this).parents(a.o.widgets),
                    o = i.data("widget-load"),
                    s = i.children(),
                    l = e(this);
                l.button("loading"), s.addClass("widget-body-ajax-loading"), setTimeout(function() {
                    l.button("reset"), s.removeClass("widget-body-ajax-loading"), a._loadAjaxFile(i, o, s)
                }, 1e3), t.preventDefault()
            }), o = null
        },
        destroy: function() {
            var i = this,
                a = "." + s;
            i.obj.find(i.o.grid + ".sortable-grid").not("[data-widget-excludegrid]").sortable("destroy"), i.widget.children("header").off(a), e(i.o.deleteSettingsKey).off(a), e(i.o.deletePositionKey).off(a), e(t).off(a), i.obj.removeData(s)
        }
    }, e.fn[s] = function(t) {
        return this.each(function() {
            var i = e(this),
                a = i.data(s);
            if (!a) {
                var l = "object" == typeof t && t;
                i.data(s, a = new o(this, l))
            }
            "string" == typeof t && a[t]()
        })
    }, e.fn[s].defaults = {
        grid: "section",
        widgets: ".jarviswidget",
        localStorage: !0,
        deleteSettingsKey: "",
        settingsKeyLabel: "Reset settings?",
        deletePositionKey: "",
        positionKeyLabel: "Reset position?",
        sortable: !0,
        buttonsHidden: !1,
        toggleButton: !0,
        toggleClass: "min-10 | plus-10",
        toggleSpeed: 200,
        onToggle: function() {},
        deleteButton: !0,
        deleteMsg: "Warning: This action cannot be undone",
        deleteClass: "trashcan-10",
        deleteSpeed: 200,
        onDelete: function() {},
        editButton: !0,
        editPlaceholder: ".jarviswidget-editbox",
        editClass: "pencil-10 | delete-10",
        editSpeed: 200,
        onEdit: function() {},
        colorButton: !0,
        fullscreenButton: !0,
        fullscreenClass: "fullscreen-10 | normalscreen-10",
        fullscreenDiff: 3,
        onFullscreen: function() {},
        customButton: !0,
        customClass: "",
        customStart: function() {},
        customEnd: function() {},
        buttonOrder: "%refresh% %delete% %custom% %edit% %fullscreen% %toggle%",
        opacity: 1,
        dragHandle: "> header",
        placeholderClass: "jarviswidget-placeholder",
        indicator: !0,
        indicatorTime: 600,
        ajax: !0,
        loadingLabel: "loading...",
        timestampPlaceholder: ".jarviswidget-timestamp",
        timestampFormat: "Last update: %m%/%d%/%y% %h%:%i%:%s%",
        refreshButton: !0,
        refreshButtonClass: "refresh-10",
        labelError: "Sorry but there was a error:",
        labelUpdated: "Last Update:",
        labelRefresh: "Refresh",
        labelDelete: "Delete widget:",
        afterLoad: function() {},
        rtl: !1,
        onChange: function() {},
        onSave: function() {},
        ajaxnav: !0
    }, e.fn.removeClassPrefix = function(t) {
        return this.each(function(i, a) {
            var o = a.className.split(" ").map(function(e) {
                return 0 === e.indexOf(t) ? "" : e
            });
            a.className = e.trim(o.join(" "))
        }), this
    }
}(jQuery, window, document);