{
    'name': 'HOSPITAL ACCOUNTING',
    'summary': 'HOSPITAL RECORD OF PATIENT VISITS',

    'author': 'Lyackh A.O.',
    'website': 'https://des-tam.ua',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.0.0.1',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': [], },
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menu_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_contact_person_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_doctor_visitor_views.xml',
        'views/hospital_diagnosis_views.xml',
        'views/hospital_disease_views.xml',
        'views/hospital_disease_aspect_views.xml',
        'views/hospital_personal_doctor_history_views.xml',
        'views/hospital_research_aspect_views.xml',
        'views/hospital_research_views.xml',
        'views/hospital_schedule_views.xml',
        'wizard/set_personal_doctor_wizard_views.xml',
        'wizard/get_report_diagnosis_wizard_views.xml',
    ],
    'demo': [
        'demo/doctor.xml',
        'demo/contact.xml',
        'demo/patient.xml',
        'demo/disease_parent.xml',
        'demo/disease.xml',
        'demo/diagnosis.xml',
        'demo/doctor_visit.xml',
    ],

    'installable': True,
    'auto_install': False,
    'aplication': False,
    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],
    'price': 0,
    'curency': 'EUR',
}
