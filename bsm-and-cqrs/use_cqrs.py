from eventsourcing.application import Application
from eventsourcing.domain import event, Aggregate


class BSM(Aggregate):
    @event('Registered')
    def __init__(self):
        self.dataType = None
        self.metadata_generatedAt = None
        self.metadata_generatedBy = None
        self.metadata_logFileName = None
        self.metadata_schemaVersion = None
        self.metadata_securityResultCode = None
        self.metadata_sanitized = None
        self.metadata_payloadType = None
        self.metadata_recordType = None
        self.metadata_serialId_streamId = None
        self.metadata_serialId_bundleSize = None
        self.metadata_serialId_bundleId = None
        self.metadata_serialId_recordId = None
        self.metadata_serialId_serialNumber = None
        self.metadata_receivedAt = None
        self.metadata_rmd_elevation = None
        self.metadata_rmd_heading = None
        self.metadata_rmd_latitude = None
        self.metadata_rmd_longitude = None
        self.metadata_rmd_speed = None
        self.smetadata_rmd_rxSource = None
        self.smetadata_bsmSource = None
        self.scoreData_msgCnt = None
        self.scoreData_id = None
        self.scoreData_secMark = None
        self.coreData_position_lat = None
        self.coreData_position_long = None
        self.coreData_elevation = None
        self.coreData_accelset_accelYaw = None
        self.coreData_accuracy_semiMajor = None
        self.coreData_accuracy_semiMinor = None
        self.coreData_transmission = None
        self.coreData_speed = None
        self.coreData_heading = None
        self.coreData_brakes_wheelBrakes_leftFront = None
        self.coreData_brakes_wheelBrakes_rightFront = None
        self.coreData_brakes_wheelBrakes_unavailable = None
        self.coreData_brakes_wheelBrakes_leftRear = None
        self.coreData_brakes_wheelBrakes_rightRear = None
        self.coreData_brakes_traction = None
        self.coreData_brakes_abs = None
        self.coreData_brakes_scs = None
        self.coreData_brakes_brakeBoost = None
        self.coreData_brakes_auxBrakes = None
        self.coreData_size = None
        self.part2_suve_cd_hpmstype = None
        self.part2_suve_cd_role = None
        self.part2_suve_vd_height = None
        self.part2_suve_vd_mass = None
        self.part2_suve_vd_trailerweight = None
        self.part2_vse_events = None
        self.part2_vse_ph_crumbdata = None
        self.part2_vse_pp_confidence = None
        self.part2_vse_pp_radiusofcurve = None
        self.part2_vse_lights = None
        self.part2_spve_vehalert_sspRights = None
        self.part2_spve_vehalert_event_sspRights = None
        self.part2_spve_vehalert_event_events = None
        self.part2_spve_vehalert_lightsUse = None
        self.part2_spve_vehalert_multi = None
        self.part2_spve_vehalert_responseType = None
        self.part2_spve_vehalert_sirenUse = None
        self.part2_spve_event_desc = None
        self.part2_spve_event_extent = None
        self.part2_spve_event_heading = None
        self.part2_spve_tr_sspRights = None
        self.part2_spve_tr_conn = None
        self.part2_spve_tr_units = None
        self.coreData_position = None
        self.bsm = []

    def set_bsm(self, bsm_section):
        self.dataType = bsm_section.get('dataType', None)
        self.metadata_generatedAt = bsm_section.get('metadata_generatedAt', None)
        self.metadata_generatedBy = bsm_section.get('metadata_generatedBy', None)
        self.metadata_logFileName = bsm_section.get('metadata_logFileName', None)
        self.metadata_schemaVersion = bsm_section.get('metadata_schemaVersion', None)
        self.metadata_securityResultCode = bsm_section.get('metadata_securityResultCode', None)
        self.metadata_sanitized = bsm_section.get('metadata_sanitized', None)
        self.metadata_payloadType = bsm_section.get('metadata_payloadType', None)
        self.metadata_recordType = bsm_section.get('metadata_recordType', None)
        self.metadata_serialId_streamId = bsm_section.get('metadata_serialId_streamId', None)
        self.metadata_serialId_bundleSize = bsm_section.get('metadata_serialId_bundleSize', None)
        self.metadata_serialId_bundleId = bsm_section.get('metadata_serialId_bundleId', None)
        self.metadata_serialId_recordId = bsm_section.get('metadata_serialId_recordId', None)
        self.metadata_serialId_serialNumber = bsm_section.get('metadata_serialId_serialNumber', None)
        self.metadata_receivedAt = bsm_section.get('metadata_receivedAt', None)
        self.metadata_rmd_elevation = bsm_section.get('metadata_rmd_elevation', None)
        self.metadata_rmd_heading = bsm_section.get('metadata_rmd_heading', None)
        self.metadata_rmd_latitude = bsm_section.get('metadata_rmd_latitude', None)
        self.metadata_rmd_longitude = bsm_section.get('metadata_rmd_longitude', None)
        self.metadata_rmd_speed = bsm_section.get('metadata_rmd_speed', None)
        self.smetadata_rmd_rxSource = bsm_section.get('smetadata_rmd_rxSource', None)
        self.smetadata_bsmSource = bsm_section.get('smetadata_bsmSource', None)
        self.scoreData_msgCnt = bsm_section.get('scoreData_msgCnt', None)
        self.scoreData_id = bsm_section.get('scoreData_id', None)
        self.scoreData_secMark = bsm_section.get('scoreData_secMark', None)
        self.coreData_position_lat = bsm_section.get('coreData_position_lat', None)
        self.coreData_position_long = bsm_section.get('coreData_position_long', None)
        self.coreData_elevation = bsm_section.get('coreData_elevation', None)
        self.coreData_accelset_accelYaw = bsm_section.get('coreData_accelset_accelYaw', None)
        self.coreData_accuracy_semiMajor = bsm_section.get('coreData_accuracy_semiMajor', None)
        self.coreData_accuracy_semiMinor = bsm_section.get('coreData_accuracy_semiMinor', None)
        self.coreData_transmission = bsm_section.get('coreData_transmission', None)
        self.coreData_speed = bsm_section.get('coreData_speed', None)
        self.coreData_heading = bsm_section.get('coreData_heading', None)
        self.coreData_brakes_wheelBrakes_leftFront = bsm_section.get('coreData_brakes_wheelBrakes_leftFront', None)
        self.coreData_brakes_wheelBrakes_rightFront = bsm_section.get('coreData_brakes_wheelBrakes_rightFront', None)
        self.coreData_brakes_wheelBrakes_unavailable = bsm_section.get('coreData_brakes_wheelBrakes_unavailable', None)
        self.coreData_brakes_wheelBrakes_leftRear = bsm_section.get('coreData_brakes_wheelBrakes_leftRear', None)
        self.coreData_brakes_wheelBrakes_rightRear = bsm_section.get('coreData_brakes_wheelBrakes_rightRear', None)
        self.coreData_brakes_traction = bsm_section.get('coreData_brakes_traction', None)
        self.coreData_brakes_abs = bsm_section.get('coreData_brakes_abs', None)
        self.coreData_brakes_scs = bsm_section.get('coreData_brakes_scs', None)
        self.coreData_brakes_brakeBoost = bsm_section.get('coreData_brakes_brakeBoost', None)
        self.coreData_brakes_auxBrakes = bsm_section.get('coreData_brakes_auxBrakes', None)
        self.coreData_size = bsm_section.get('coreData_size', None)
        self.part2_suve_cd_hpmstype = bsm_section.get('part2_suve_cd_hpmstype', None)
        self.part2_suve_cd_role = bsm_section.get('part2_suve_cd_role', None)
        self.part2_suve_vd_height = bsm_section.get('part2_suve_vd_height', None)
        self.part2_suve_vd_mass = bsm_section.get('part2_suve_vd_mass', None)
        self.part2_suve_vd_trailerweight = bsm_section.get('part2_suve_vd_trailerweight', None)
        self.part2_vse_events = bsm_section.get('part2_vse_events', None)
        self.part2_vse_ph_crumbdata = bsm_section.get('part2_vse_ph_crumbdata', None)
        self.part2_vse_pp_confidence = bsm_section.get('part2_vse_pp_confidence', None)
        self.part2_vse_pp_radiusofcurve = bsm_section.get('part2_vse_pp_radiusofcurve', None)
        self.part2_vse_lights = bsm_section.get('part2_vse_lights', None)
        self.part2_spve_vehalert_sspRights = bsm_section.get('part2_spve_vehalert_sspRights', None)
        self.part2_spve_vehalert_event_sspRights = bsm_section.get('part2_spve_vehalert_event_sspRights', None)
        self.part2_spve_vehalert_event_events = bsm_section.get('part2_spve_vehalert_event_events', None)
        self.part2_spve_vehalert_lightsUse = bsm_section.get('part2_spve_vehalert_lightsUse', None)
        self.part2_spve_vehalert_multi = bsm_section.get('part2_spve_vehalert_multi', None)
        self.part2_spve_vehalert_responseType = bsm_section.get('part2_spve_vehalert_responseType', None)
        self.part2_spve_vehalert_sirenUse = bsm_section.get('part2_spve_vehalert_sirenUse', None)
        self.part2_spve_event_desc = bsm_section.get('part2_spve_event_desc', None)
        self.part2_spve_event_extent = bsm_section.get('part2_spve_event_extent', None)
        self.part2_spve_event_heading = bsm_section.get('part2_spve_event_heading', None)
        self.part2_spve_tr_sspRights = bsm_section.get('part2_spve_tr_sspRights', None)
        self.part2_spve_tr_conn = bsm_section.get('part2_spve_tr_conn', None)
        self.part2_spve_tr_units = bsm_section.get('part2_spve_tr_units', None)
        self.coreData_position = bsm_section.get('coreData_position', None)

    @event('BSMSaved')
    def add_bsm(self, bsm):
        self.bsm.append(bsm)


class BSMLogger(Application):
    def register_bsm(self, bsm_section):
        bsm = BSM()
        bsm.set_bsm(bsm_section)
        self.save(bsm)
        return bsm.id

    def add_bsm(self, bsm_id):
        bsm = self.repository.get(bsm_id)
        bsm.add_bsm(bsm=bsm)
        self.save(bsm)

    def get_bsm(self, bsm_id):
        bsm = self.repository.get(bsm_id)
        return {'name': bsm.metadata_generatedBy, 'tricks': tuple(bsm)}


if __name__ == '__main__':
    application = BSMLogger()
    bsm = {"dataType": None, "part2_spve_vehalert_lightsUse": None}
    bsm_id = application.register_bsm(bsm)
    print(bsm_id)
