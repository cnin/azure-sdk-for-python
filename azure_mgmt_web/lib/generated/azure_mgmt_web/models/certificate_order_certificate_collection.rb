# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Collection of ceritificateorder certificates
    #
    class CertificateOrderCertificateCollection

      include MsRestAzure

      # @return [Array<CertificateOrderCertificate>] Collection of resources
      attr_accessor :value

      # @return [String] Link to next page of resources
      attr_accessor :next_link


      #
      # Mapper for CertificateOrderCertificateCollection class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'CertificateOrderCertificateCollection',
          type: {
            name: 'Composite',
            class_name: 'CertificateOrderCertificateCollection',
            model_properties: {
              value: {
                required: false,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'CertificateOrderCertificateElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'CertificateOrderCertificate'
                      }
                  }
                }
              },
              next_link: {
                required: false,
                serialized_name: 'nextLink',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end