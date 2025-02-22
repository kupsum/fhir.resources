# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Group
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import group


def impl_group_1(inst):
    assert inst.characteristic[0].code.text == "gender"
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].valueCodeableConcept.text == "mixed"
    assert inst.characteristic[1].code.text == "owner"
    assert inst.characteristic[1].exclude is False
    assert inst.characteristic[1].valueCodeableConcept.text == "John Smith"
    assert inst.code.text == "Horse"
    assert inst.id == "101"
    assert (
        inst.identifier[0].system
        == "http://someveterinarianclinic.org/fhir/NamingSystem/herds"
    )
    assert inst.identifier[0].value == "12345"
    assert inst.membership == "enumerated"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "John's herd"
    assert inst.quantity == 25
    assert inst.text.status == "additional"
    assert inst.type == "animal"


def test_group_1(base_settings):
    """No. 1 tests collection for Group.
    Test File: group-example.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example.json"
    inst = group.Group.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Group" == inst.resource_type

    impl_group_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_1(inst2)


def impl_group_2(inst):
    assert inst.id == "102"
    assert inst.member[0].entity.reference == "Patient/pat1"
    assert inst.member[0].period.start == fhirtypes.DateTime.validate("2014-10-08")
    assert inst.member[1].entity.reference == "Patient/pat2"
    assert inst.member[1].inactive is True
    assert inst.member[1].period.start == fhirtypes.DateTime.validate("2015-04-02")
    assert inst.member[2].entity.reference == "Patient/pat3"
    assert inst.member[2].period.start == fhirtypes.DateTime.validate("2015-08-06")
    assert inst.member[3].entity.reference == "Patient/pat4"
    assert inst.member[3].period.start == fhirtypes.DateTime.validate("2015-08-06")
    assert inst.membership == "enumerated"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "additional"
    assert inst.type == "person"


def test_group_2(base_settings):
    """No. 2 tests collection for Group.
    Test File: group-example-member.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example-member.json"
    inst = group.Group.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Group" == inst.resource_type

    impl_group_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_2(inst2)


def impl_group_3(inst):
    assert inst.characteristic[0].code.coding[0].code == "attributed-to"
    assert inst.characteristic[0].code.coding[0].system == "http://example.org"
    assert inst.characteristic[0].code.text == "Patients primarily attributed to"
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].valueReference.reference == "Practitioner/123"
    assert inst.id == "example-patientlist"
    assert inst.membership == "enumerated"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "additional"
    assert inst.type == "person"


def test_group_3(base_settings):
    """No. 3 tests collection for Group.
    Test File: group-example-patientlist.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example-patientlist.json"
    inst = group.Group.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Group" == inst.resource_type

    impl_group_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_3(inst2)


def impl_group_4(inst):
    assert inst.active is True
    assert inst.characteristic[0].code.text == "gender"
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].valueCodeableConcept.text == "female"
    assert inst.code.coding[0].code == "388393002"
    assert inst.code.coding[0].display == "Genus Sus (organism)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[1].code == "POR"
    assert inst.code.coding[1].display == "porcine"
    assert inst.code.coding[1].system == "https://www.aphis.usda.gov"
    assert inst.code.text == "Porcine"
    assert inst.extension[0].url == "http://example.org/fhir/StructureDefinition/owner"
    assert inst.extension[0].valueReference.display == "Peter Chalmers"
    assert inst.extension[0].valueReference.reference == "RelatedPerson/peter"
    assert inst.id == "herd1"
    assert inst.identifier[0].system == "https://vetmed.iastate.edu/vdl"
    assert inst.identifier[0].value == "20171120-1234"
    assert inst.membership == "enumerated"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Breeding herd"
    assert inst.quantity == 2500
    assert inst.text.status == "generated"
    assert inst.type == "animal"


def test_group_4(base_settings):
    """No. 4 tests collection for Group.
    Test File: group-example-herd1.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example-herd1.json"
    inst = group.Group.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Group" == inst.resource_type

    impl_group_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_4(inst2)


def impl_group_5(inst):
    assert inst.active is True
    assert inst.description == "[markdown]"
    assert inst.id == "groupDenovoFamily"
    assert inst.identifier[0].assigner.display == "Child Hospital"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2021-01-01")
    assert (
        inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/groups"
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].display == "Medical record number"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "11111"
    assert inst.managingEntity.reference == "Practitioner/practitioner02"
    assert inst.member[0].entity.reference == "Patient/proband"
    assert inst.member[0].inactive is False
    assert inst.member[0].period.start == fhirtypes.DateTime.validate(
        "2021-01-01T01:01:10-06:00"
    )
    assert inst.member[1].entity.reference == "RelatedPerson/relatedPersonDenovoMother"
    assert inst.member[1].inactive is False
    assert inst.member[1].period.start == fhirtypes.DateTime.validate(
        "2021-01-01T01:01:10-06:00"
    )
    assert inst.member[2].entity.reference == "RelatedPerson/relatedPersonDenovoFather"
    assert inst.member[2].inactive is False
    assert inst.member[2].period.start == fhirtypes.DateTime.validate(
        "2021-01-01T01:01:10-06:00"
    )
    assert inst.membership == "enumerated"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Denovo Mutation Example Group"
    assert inst.quantity == 3
    assert inst.text.status == "additional"
    assert inst.type == "person"


def test_group_5(base_settings):
    """No. 5 tests collection for Group.
    Test File: Group-denovoFamily.json
    """
    filename = base_settings["unittest_data_dir"] / "Group-denovoFamily.json"
    inst = group.Group.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Group" == inst.resource_type

    impl_group_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_5(inst2)
