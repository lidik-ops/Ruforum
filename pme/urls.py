from django.urls import path
from pme.views import (
    UnitsListView,
    CreateUnitView,
    UnitDetailView,
    UnitUpdateView,
    UnitDeleteView,
    SourceoffundingsListView,
    CreateSourceoffundingView,
    SourceoffundingDetailView,
    SourceoffundingUpdateView,
    SourceoffundingDeleteView,
    ResultareasListView,
    CreateResultareaView,
    ResultareaDetailView,
    ResultareaUpdateView,
    ResultareaDeleteView,
    FinancialYearsListView,
    CreateFinancialYearView,
    FinancialYearDetailView,
    FinancialYearUpdateView,
    FinancialYearDeleteView,
    WorkplansListView,
    CreateWorkplanView,
    WorkplanDetailView,
    WorkplanUpdateView,
    WorkplanDeleteView,
    ActivitysListView,
    CreateActivityView,
    ActivityDetailView,
    ActivityUpdateView,
    ActivityDeleteView,
    ExpectedoutputsListView,
    CreateExpectedoutputView,
    ExpectedoutputDetailView,
    ExpectedoutputUpdateView,
    ExpectedoutputDeleteView,
    TasksListView,
    CreateTaskView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    IndicatorsListView,
    CreateIndicatorView,
    IndicatorDetailView,
    IndicatorUpdateView,
    IndicatorDeleteView,
    ActivityOutputListView,
    CreateActivityoutputView,ActivityoutputDeleteView,
    ActivityoutputUpdateView,CreateTaskReportView,TaskReportListView,TaskReportUpdateView,TaskReportDeleteView
    ,FrameworkUnitsListView,CreateFrameworkUnitView,FrameworkUnitUpdateView,FrameworkUnitDeleteView
    ,FrameworkListView,FrameworkListView,CreateFrameworkView,FrameworkUpdateView,FrameworkDeleteView,
    FrameworkResultListView,CreateFrameworkResultView,FrameworkResultDetailView,FrameworkResultUpdateView,
    FrameworkResultDeleteView

)

app_name = 'pme'


urlpatterns = [
    path('units/', UnitsListView.as_view(), name='unit_list'),
    path('create_unit/', CreateUnitView.as_view(), name='add_unit'),
    path('<int:pk>/view_unit/', UnitDetailView.as_view(), name="view_unit"),
    path('<int:pk>/edit_unit/', UnitUpdateView.as_view(), name="edit_unit"),
    path('<int:pk>/delete_unit/',
         UnitDeleteView.as_view(),
         name="remove_unit"),

    path('sourceoffundings/', SourceoffundingsListView.as_view(), name='sourceoffunding_list'),
    path('create_sourceoffunding/', CreateSourceoffundingView.as_view(), name='add_sourceoffunding'),
    path('<int:pk>/view_sourceoffunding/', SourceoffundingDetailView.as_view(), name="view_sourceoffunding"),
    path('<int:pk>/edit_sourceoffunding/', SourceoffundingUpdateView.as_view(), name="edit_sourceoffunding"),
    path('<int:pk>/delete_sourceoffunding/',
         SourceoffundingDeleteView.as_view(),
         name="remove_sourceoffunding"),

    path('flagships/', ResultareasListView.as_view(), name='resultarea_list'),
    path('create_resultarea/', CreateResultareaView.as_view(), name='add_resultarea'),
    path('<int:pk>/view_resultarea/', ResultareaDetailView.as_view(), name="view_resultarea"),
    path('<int:pk>/edit_resultarea/', ResultareaUpdateView.as_view(), name="edit_resultarea"),
    path('<int:pk>/delete_resultarea/',
         ResultareaDeleteView.as_view(),
         name="remove_resultarea"),

    path('financialyears/', FinancialYearsListView.as_view(), name='financialyear_list'),
    path('create_financialyear/', CreateFinancialYearView.as_view(), name='add_financialyear'),
    path('<int:pk>/view_financialyear/', FinancialYearDetailView.as_view(), name="view_financialyear"),
    path('<int:pk>/edit_financialyear/', FinancialYearUpdateView.as_view(), name="edit_financialyear"),
    path('<int:pk>/delete_financialyear/',
         FinancialYearDeleteView.as_view(),
         name="remove_financialyear"),

    path('workplans/', WorkplansListView.as_view(), name='workplan_list'),
    path('create_workplan/', CreateWorkplanView.as_view(), name='add_workplan'),
    path('<int:pk>/view_workplan/', WorkplanDetailView.as_view(), name="view_workplan"),
    path('<int:pk>/edit_workplan/', WorkplanUpdateView.as_view(), name="edit_workplan"),
    path('<int:pk>/delete_workplan/',
         WorkplanDeleteView.as_view(),
         name="remove_workplan"),

    path('activities/', ActivitysListView.as_view(), name='activity_list'),
    path('create_activity/', CreateActivityView.as_view(), name='add_activity'),
    path('<int:pk>/view_activity/', ActivityDetailView.as_view(), name="view_activity"),
    path('<int:pk>/edit_activity/', ActivityUpdateView.as_view(), name="edit_activity"),
    path('<int:pk>/delete_activity/',
         ActivityDeleteView.as_view(),
         name="remove_activity"),

    path('outputs/', ExpectedoutputsListView.as_view(), name='output_list'),
    path('create_output/', CreateExpectedoutputView.as_view(), name='add_output'),
    path('<int:pk>/view_output/', ExpectedoutputDetailView.as_view(), name="view_output"),
    path('<int:pk>/edit_output/', ExpectedoutputUpdateView.as_view(), name="edit_output"),
    path('<int:pk>/delete_output/',
         ExpectedoutputDeleteView.as_view(),
         name="remove_output"),

    path('tasks/', TasksListView.as_view(), name='task_list'),
    path('create_task/', CreateTaskView.as_view(), name='add_task'),
    path('<int:pk>/view_task/', TaskDetailView.as_view(), name="view_task"),
    path('<int:pk>/edit_task/', TaskUpdateView.as_view(), name="edit_task"),
    path('<int:pk>/delete_task/',
         TaskDeleteView.as_view(),
         name="remove_task"),
    path('<int:task_pk>/task/status',CreateTaskReportView.as_view(),name='add_task_status'),
    path('tasks/reports', TaskReportListView.as_view(), name='task_reports'),
    path('<int:pk>/edit_task_report/', TaskReportUpdateView.as_view(), name="edit_task_report"),
    path('<int:pk>/delete_task_report/', TaskReportDeleteView.as_view(), name="delete_task_report"),


    path('indicators/', IndicatorsListView.as_view(), name='indicator_list'),
    path('create_indicator/', CreateIndicatorView.as_view(), name='add_indicator'),
    path('<int:pk>/view_indicator/', IndicatorDetailView.as_view(), name="view_indicator"),
    path('<int:pk>/edit_indicator/', IndicatorUpdateView.as_view(), name="edit_indicator"),
    path('<int:pk>/delete_indicator/',
         IndicatorDeleteView.as_view(),
         name="remove_indicator"),

    path('activity_output/', ActivityOutputListView.as_view(),name="activity_output_list"),
    path('create_activity_output/', CreateActivityoutputView.as_view(), name='add_activityoutput'),
    path('<int:pk>/edit_activity_output/', ActivityoutputUpdateView.as_view(), name="edit_activityoutput"),
    path('<int:pk>/delete_activity_output/',
         ActivityoutputDeleteView.as_view(),
         name="remove_activityoutput"),

    path('framework-units/', FrameworkUnitsListView.as_view(), name='framework_unit_list'),
    path('create_framework/unit/', CreateFrameworkUnitView.as_view(), name='add_framework_unit'),
    path('<int:pk>/edit/framwork_unit/', FrameworkUnitUpdateView.as_view(), name="edit_framework_unit"),
    path('<int:pk>/delete_framework_unit/',FrameworkUnitDeleteView.as_view(),
         name="remove_framework_unit"),


    path('frameworks/', FrameworkListView.as_view(), name='framework_list'),
    path('create_framework/', CreateFrameworkView.as_view(), name='add_framework'),
    path('<int:pk>/edit/framwork/', FrameworkUpdateView.as_view(), name="edit_framework"),
    path('<int:pk>/delete_framework/',FrameworkDeleteView.as_view(), name="remove_framework"),

    path('framework/results/', FrameworkResultListView.as_view(), name='framework_result_list'),
    path('create_framework_result/', CreateFrameworkResultView.as_view(), name='add_framework_result'),
    path('<int:pk>/view_framework_result/', FrameworkResultDetailView.as_view(), name="view_framework_result"),
    path('<int:pk>/edit_framework_result/', FrameworkResultUpdateView.as_view(), name="edit_framework_result"),
    path('<int:pk>/delete_framework_result/',
         FrameworkResultDeleteView.as_view(),
         name="remove_framework_result"),


]
