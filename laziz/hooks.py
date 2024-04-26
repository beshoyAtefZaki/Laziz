from . import __version__ as app_version

app_name = "laziz"
app_title = "Laziz"
app_publisher = "beshoy atef"
app_description = "Laziz"
app_email = "beshoy@dynamic.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/laziz/css/laziz.css"
app_include_js = "/assets/laziz/js/laziz.js"

# include js, css files in header of web template
# web_include_css = "/assets/laziz/css/laziz.css"
# web_include_js = "/assets/laziz/js/laziz.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "laziz/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"User" : "public/js/user.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Accounts Manager": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
	"methods": ["laziz.utils.jinja_methods", "laziz.utils.jinja_methods_2"],
	# "filters": "laziz.utils.jinja_filters"
}

# Installation
# ------------

# before_install = "laziz.install.before_install"
# after_install = "laziz.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "laziz.uninstall.before_uninstall"
# after_uninstall = "laziz.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "laziz.utils.before_app_install"
# after_app_install = "laziz.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "laziz.utils.before_app_uninstall"
# after_app_uninstall = "laziz.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "laziz.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#         "5 0 * * *": [
# 		"laziz.tasks.all"
    
#         ]
# }

#	"all": [
#		"laziz.tasks.all"
#	],
#	"daily": [
#		"laziz.tasks.daily"
#	],
#	"hourly": [
#		"laziz.tasks.hourly"
#	],
#	"weekly": [
#		"laziz.tasks.weekly"
#	],
#	"monthly": [
#		"laziz.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "laziz.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "laziz.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "laziz.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["laziz.utils.before_request"]
# after_request = ["laziz.utils.after_request"]

# Job Events
# ----------
# before_job = ["laziz.utils.before_job"]
# after_job = ["laziz.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"laziz.auth.validate"
# ]
